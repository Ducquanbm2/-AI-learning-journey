import cv2
import numpy as np

img = cv2.imread(r'D:\python\Machine Learning\Neural Network\Color_image.webp', 1)
img_gray = cv2.imread(r'D:\python\Machine Learning\Neural Network\Gray_image.webp', 0)
"""
if img is None:
    print("Không thể tải hình ảnh. Kiểm tra lại đường dẫn.")
else: 
    cv2.imshow("test", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
"""

img2 = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
"""
img2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
cv2.imshow("test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
Using function to convert color image to gray image
"""


# BGR: 11 59 30
"""
for i in range(0, img2.shape[0]):
    for j in range(0, img2.shape[1]):
        img2[i][j] = img[i][j][0] * 0.11 + img[i][j][1] * 0.59 + img[i][j][1] * 0.3


cv2.imshow("test", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
# Resize image
"""

new_width = 600
scale = int(int(img.shape[0]) / int(img.shape[1]))

new_heigh = new_width * scale
img3 = np.zeros((new_heigh, new_width), dtype=np.uint8)
img3 = cv2.resize(img, (new_heigh, new_width))
cv2.imshow("new size", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

# Convolution

img_gray = cv2.GaussianBlur(img_gray, (3,3), 0)
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])


def convolution(x, y):
    val = 0
    for i in range(0, 3):
        for j in range(0, 3):
            val = val + kernel[i][j] * img_gray[x + i][y + j]
    return val


    
img4 = np.zeros((img.shape[0] - 2, img.shape[1] - 2), dtype=float)

for k in range(0, 1):
    for i in range(1, img_gray.shape[0] - 1):
        for j in range(1, img_gray.shape[1] - 1):
            convolution_value = convolution(i - 1, j - 1)
            img4[i - 1][j - 1] = convolution_value

img4 = np.clip(img4, 0, 255).astype(np.uint8)

cv2.imshow("image was convoluted", img4)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
# Làm mờ trước khi sharpen để giảm nhiễu
blurred = cv2.GaussianBlur(img, (3,3), 0)

# Kernel sharpen nhẹ
sharpen_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

# Áp dụng bộ lọc
sharpened = cv2.filter2D(blurred, -1, sharpen_kernel)

# Đảm bảo giá trị pixel nằm trong khoảng hợp lệ
sharpened = np.clip(sharpened, 0, 255).astype(np.uint8)

# Hiển thị ảnh
cv2.imshow("Sharpened Image", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""