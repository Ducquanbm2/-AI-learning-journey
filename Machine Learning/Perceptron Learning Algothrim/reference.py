import numpy as np

# Dữ liệu đầu vào (thêm bias)
X = np.array([[1, 1, 0],
              [1, 1, 1],
              [1, 0, 1],
              [1, 0, 0]])

# Chuyển đổi nhãn từ {0,1} sang {-1,1}
Y_notAnd = 2 * np.array([[1], [0], [1], [1]]) - 1
Y_Or = 2 * np.array([[1], [1], [1], [0]]) - 1
Y = 2 * np.array([[1], [0], [1], [0]]) - 1  # XOR

# Hàm kích hoạt sign {-1,1}
def sgn(X, w):
    return np.where(X @ w >= 0, 1, -1)

# Hàm học Perceptron
def Perceptron_learning(w, X, Y, max_iters=100):
    for _ in range(max_iters):
        misclassified = np.where(Y.flatten() != sgn(X, w).flatten())[0]
        if len(misclassified) == 0:
            return w  # Nếu không có điểm nào sai thì dừng
        j = np.random.choice(misclassified)
        w += (Y[j] * X[j].reshape(-1, 1))  # Cập nhật trọng số
    return w

# Khởi tạo trọng số ngẫu nhiên
np.random.seed(14)
w1 = np.random.rand(3, 1)  # Trọng số tầng ẩn 1
w2 = np.random.rand(3, 1)  # Trọng số tầng ẩn 2

# Huấn luyện tầng ẩn
w1_trained = Perceptron_learning(w1, X, Y_notAnd)
w2_trained = Perceptron_learning(w2, X, Y_Or)



print(sgn(X, w1_trained))



X_hidden = np.hstack([
    np.ones((X.shape[0], 1)),  
    sgn(X, w1_trained),  
    sgn(X, w2_trained)   
])

w_final = Perceptron_learning(np.random.rand(3, 1), X_hidden, Y)

result = sgn(X_hidden, w_final)
print(result)
