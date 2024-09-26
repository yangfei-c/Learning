import cv2
import numpy as np

# 读取图像
img = cv2.imread("../img/ChenYao.jpg")
if img is None:
    print("无法读取图像，请检查文件路径。")
    exit()

# 将图像转换为 HSV 色彩空间
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 定义肤色的 HSV 范围
# 可以根据实验调整范围以适应不同的肤色
lower_skin = np.array([0, 30, 60], dtype=np.uint8)   # 定义下界
upper_skin = np.array([20, 150, 255], dtype=np.uint8)  # 定义上界

# 生成肤色掩膜
skin_mask = cv2.inRange(hsv_img, lower_skin, upper_skin)

# 将掩膜应用到原图像，提取肤色区域
skin = cv2.bitwise_and(img, img, mask=skin_mask)

# 可视化：将非肤色区域涂成白色
visualization = img.copy()
visualization[skin_mask == 0] = [255, 255, 255]  # 非肤色区域涂白

# 显示结果
cv2.imshow("Original Image", img)
cv2.imshow("Detected Skin", skin)
cv2.imshow("Skin Visualization", visualization)
cv2.waitKey(0)
cv2.destroyAllWindows()
