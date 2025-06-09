import numpy as np
import matplotlib.pyplot as plt


np.random.seed(13)
N = 100  

a, b = np.random.randn(2)
c = np.random.uniform(-1, 1)

X = np.random.uniform(-1, 1, (N, 2))  

y = np.sign(a * X[:, 0] + b * X[:, 1] + c)

X = np.hstack((np.ones((N, 1)), X))  

w = np.random.randn(3)  




def Predicted(X, w):
    return np.sign(X @ w)




def Perceptron_Learning(w, X, y):
    for i in range(0, 30):
        misclassified = np.where(Predicted(X, w) != y)[0]
        if len(misclassified) == 0:
            return w
        i = np.random.choice(misclassified)
        w += y[i] * X[i]
    return w


w_final = Perceptron_Learning(w, X, y)


def plot_data(X, y, w, title="PLA Result"):
    plt.figure(figsize=(6,6))
    plt.scatter(X[y == 1, 1], X[y == 1, 2], marker='o', color='blue', label="Class +1")
    plt.scatter(X[y == -1, 1], X[y == -1, 2], marker='x', color='red', label="Class -1")
    
    # Vẽ đường thẳng phân tách: w0 + w1*x + w2*y = 0 <=> y = -(w0 + w1*x) / w2
    x_vals = np.linspace(-1, 1, 100)
    y_vals = -(w[0] + w[1] * x_vals) / w[2]
    plt.plot(x_vals, y_vals, 'k-', label="Decision Boundary")
    
    plt.legend()
    plt.title(title)
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.grid()
    plt.show()

# Vẽ kết quả cuối cùng
plot_data(X, y, w_final, title=f"PLA Converged")

