import sqlite3
import re

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer


db = sqlite3.connect('regression.sqlite')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS model_params")
cursor.execute("DROP TABLE IF EXISTS model_coefs")
cursor.execute("DROP TABLE IF EXISTS model_results")

cursor.execute('''CREATE TABLE model_params (
               id INTEGER,
               desc TEXT,
               param_name TEXT,
               value REAL)''')

cursor.execute('''CREATE TABLE model_coefs (
               id INTEGER,
               desc TEXT,
               feature_name TEXT,
               value REAL)''')

cursor.execute('''CREATE TABLE model_results (
               id INTEGER,
               desc TEXT,
               train_score REAL,
               test_score REAL)''')

db.commit()

# Load data
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=87)


def save_to_database(model_id, model_desc, db, model, X_train, X_test, y_train, y_test):
    connect = sqlite3.connect(db)

    ###### To get the model parameters
    params = model.get_params()
    model_params_keys = str(list(params.keys()))
    model_params_values = str(list(params.values()))
    cursor.execute('''INSERT INTO model_params
                    (id, desc, param_name, value)
                    VALUES (?, ?, ?, ?)''',
                    [model_id, model_desc, model_params_keys, model_params_values])


    ######## To get the model coefficinets
    feature_name, coef = list(X_train.columns), model.coef_
    intercept = model.intercept_
    feature_name.append("intercept")
    feature_name = str(feature_name)
    feature_value = str(np.append(coef, intercept).tolist())
    cursor.execute('''INSERT INTO model_coefs
                    (id, desc, feature_name, value)
                    VALUES (?, ?, ?, ?)''', [model_id, model_desc, feature_name, feature_value])


    ######## To get the model results
    cursor.execute('''INSERT INTO model_results
                    (id, desc, train_score, test_score)
                    VALUES (?, ?, ?, ?)''',
                    [model_id, model_desc, model.score(X_train, y_train), model.score(X_test, y_test)])


# Baseline logistic regression model
baseline_model = LogisticRegression(solver='liblinear')
baseline_model.fit(X_train, y_train)
save_to_database(1, "Baseline model", 'regression.sqlite', baseline_model, X_train, X_test, y_train, y_test)

# Reduced logistic regression model
feature_cols = ['mean radius',
                'texture error',
                'worst radius',
                'worst compactness',
                'worst concavity']
reduced_model = LogisticRegression(solver='liblinear')
reduced_model.fit(X_train[feature_cols], y_train)
save_to_database(2, "Reduced model", 'regression.sqlite', reduced_model, X_train[feature_cols], X_test[feature_cols], y_train, y_test)

# Logistic regression model with L1 penalty
l1_penalty_model = LogisticRegression(solver='liblinear', penalty='l1', max_iter=500)
l1_penalty_model.fit(X_train, y_train)
save_to_database(3, "L1 penalty model", 'regression.sqlite', l1_penalty_model, X_train, X_test, y_train, y_test)


query = '''SELECT id, MAX(test_score) FROM model_results'''
q = cursor.execute(query).fetchall()
print("Best model id: " + str(q[0][0]))
print("Best validation score: " + str(q[0][1]))

query = '''SELECT * FROM model_coefs where id == 3'''
q = cursor.execute(query).fetchall()
feature_names = q[0][2]
feature_names = re.findall(r"'(.*?)'", feature_names)
feature_values = q[0][3][1:-1].split(',')
for i in range(len(feature_names)):
    feature_values[i] = float(feature_values[i].strip())
    print(feature_names[i], ': ', feature_values[i])


dummy_model = LogisticRegression(solver='liblinear')
dummy_model.fit(X_train, y_train)
dummy_model.coef_ = np.asarray([feature_values[:-1]])
dummy_model.intercept_ = np.asarray([feature_values[-1]])
print("The dummy model score is " + str(dummy_model.score(X_test, y_test)))

db.close()
