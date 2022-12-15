from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
from dataclasses import dataclass

@dataclass
class PolyRegModel:
    degree: int
    reg: LinearRegression = LinearRegression()

    def __post_init__(self):
        self.poly = PolynomialFeatures(degree = self.degree)
        self.reg = LinearRegression()

    @classmethod
    def _reformat_X(cls, X):
        return np.array(X).reshape(-1, 1)

    def train(self, X, y):
        X_poly = self.poly.fit_transform(self._reformat_X(X))
        self.reg.fit(X_poly, y)

    def predict(self, X):
        X_poly = self.poly.fit_transform(self._reformat_X(X))
        return self.reg.predict(X_poly)


PolyRegModel(4)