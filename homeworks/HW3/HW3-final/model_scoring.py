from sklearn import datasets
from sklearn.model_selection import train_test_split
from Regression import Regression as rgs
from Regression import RidgeRegression as rr
from Regression import LinearRegression as lr

dataset = datasets.load_boston()
X_train, X_test, y_train, y_test = train_test_split(dataset["data"],
                                                    dataset["target"],
                                                    test_size=0.2,
                                                    random_state=42)

alpha = 0.1
model1 = lr()
model2 = rr()
model2.set_params(alpha = alpha)
models = [model1, model2]

for model in models:
    model.fit(X_train, y_train)
    print(model.get_params())
    model.predict(X_test)
    score_R2 = model.score(X_test, y_test)
    print("The R^2 value is ", score_R2, '\n')
