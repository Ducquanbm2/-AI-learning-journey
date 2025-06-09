import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


X = np.array([0.8, 0.5]) # numpy array
W1 = np.random.randn(2, 1) 
b1 = np.random.randn(1)
W2 = np.random.randn(2, 1)
b2 = np.random.randn(1)
W_output = np.random.randn(2, 1)
b_output = np.random.randn(1)


def hidden_layer(X, type):
    if type == 1:
        value = np.dot(X, W1) + b1
        return sigmoid(value)
    else:
        value = np.dot(X, W2) + b2
        return sigmoid(value)



X1_output = hidden_layer(X, 1)
X2_output = hidden_layer(X, 2)
X_output = np.array([X1_output[0], X2_output[0]])
value_output = np.dot(X_output, W_output) + b_output
print("Output value is ", value_output)
    