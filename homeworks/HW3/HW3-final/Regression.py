import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split


class Regression():

    def __init__(self):
        self.params = {
            'coefficients':[],
            'intercept':[]
        }

    def get_params(self):
        return self.params


    def set_params(self, **kwargs):
        pass

    def fit(self, X, y):
        raise NotImplementedError

    def predict(self, X):
        para_co = np.array(self.params['coefficients'], dtype=np.float32)
        para_int = np.array(self.params['intercept'], dtype=np.float32)
        return X.dot(para_co) + para_int

    def score(self, X, y):
        sst = np.sum(np.square(y - np.mean(y)))
        sse = np.sum(np.square(y - self.predict(X)))
        return 1 - sse / sst

class LinearRegression(Regression):
    def fit(self, X, y):

        X = np.array(X, dtype=np.float32)
        X_withones = np.append(X, np.ones([X.shape[0], 1]), 1)
        xtx = (np.transpose(X_withones)).dot(X_withones)

        beta_hat_ols = np.linalg.pinv(xtx).dot(np.transpose(X_withones)).dot(y)
        self.params['coefficients'] = beta_hat_ols[0 : len(beta_hat_ols) - 1]
        self.params['intercept'] = beta_hat_ols[-1]
        self.X_withones = X_withones
        return self.params

class RidgeRegression(LinearRegression):
    def fit(self, X, y):
        X = np.array(X, dtype=np.float32)
        row_num, column_num = X.shape
        X_withones = np.append(X, np.ones([X.shape[0], 1]), 1) 
        xtx = (np.transpose(X_withones)).dot(X_withones)
        gamma = self.params['alpha'] * (np.identity(column_num + 1))
        gtg = np.transpose(gamma).dot(gamma)
        beta_hat_rr = np.linalg.pinv(xtx + gtg).dot(np.transpose(X_withones)).dot(y)
        self.params['coefficients'] = beta_hat_rr[0 : len(beta_hat_rr) - 1]
        self.params['intercept'] = beta_hat_rr[-1]
        self.X_withones = X_withones
        return self.params

    def set_params(self, **kwargs):
        for key, value in kwargs.items():
            self.params[key] = value
        return self.params
