import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from Regression import Regression as rgs
from Regression import RidgeRegression as rr
from Regression import LinearRegression as lr



boston = datasets.load_boston()
X_train, X_test, y_train, y_test = train_test_split(boston["data"],
                                                    boston["target"],
                                                    test_size=0.2,
                                                    random_state=42)

alphas = np.linspace(0.05, 1, 10)

rr = rr()
lr = lr()
rr_scores = []
lr_scores = []

for a in alphas:
    rr.set_params(alpha = a)
    rr.fit(X_train, y_train)
    rr_score = rr.score(X_test, y_test)
    rr_scores.append(rr_score)

    lr.set_params(alpha = a)
    lr.fit(X_train, y_train)
    lr_score = lr.score(X_test, y_test)
    lr_scores.append(lr_score)


plt.figure()
plt.plot(alphas, rr_scores, label = "Ridge Regression")
plt.plot(alphas, lr_scores, label = "Linear Regression")
plt.legend
plt.xlabel(r"$\alpha$")
plt.ylabel("$R^2$")
plt.title("R^2 - alpha")
plt.grid()
plt.savefig("P1F.png")
plt.show()
