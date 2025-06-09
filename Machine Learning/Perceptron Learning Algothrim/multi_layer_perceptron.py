import numpy as np
import matplotlib.pyplot as plt

X = np.array([[1, 1, 0],[1, 1, 1],[1, 0, 1],[1, 0, 0]])
Y_notAnd = 2 * np.array([[1], [0], [1], [1]]) - 1
Y_Or = 2 * np.array([[1], [1], [1], [0]]) - 1
Y = 2 * np.array([[1], [0], [1], [0]]) - 1



np.random.seed(20)
w1 = np.random.rand(3, 1)
w2 = np.random.rand(3, 1)

def sgn(X, w):
    return np.where(X @ w >= 0, 1, -1)

def predict(X, w):
    return np.where(X @ w >= 0, 1, 0)


def Perceptron_learning(w, X, Y):
    for i in range(0, 50):
        misclassified = np.where(Y != sgn(X, w))[0]
        if len(misclassified) == 0:
            return w
        j = np.random.choice(misclassified)
        w += (Y[j] * X[j].reshape(3, 1))
    return w




w_after_hiden1 = np.random.rand(3, 1)
X_after_hiden1 = np.array([[1],[1],[1],[1]])
X_after_hiden1 = np.concatenate((X_after_hiden1, sgn(X, Perceptron_learning(w1, X, Y_notAnd))), axis=1)
X_after_hiden1 = np.concatenate((X_after_hiden1, sgn(X, Perceptron_learning(w2, X, Y_Or))), axis=1)
w_final = Perceptron_learning(w_after_hiden1, X_after_hiden1, Y)


result = predict(X_after_hiden1, w_final)   
print(result)

