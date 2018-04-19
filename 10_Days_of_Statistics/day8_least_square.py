from sklearn import linear_model
import numpy as np

grades = np.array([list(map(int, input().split(" "))) for i in range(5)])
x = np.asarray(grades[:, 0]).reshape(-1, 1)
lm = linear_model.LinearRegression()
lm.fit(x, grades[:, 1])
print(round(lm.intercept_ + lm.coef_[0]*80, 3))
