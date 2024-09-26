import cv2
import numpy as np

# 读取图像
img = cv2.imread("../img/ChenYao.jpg")

if img is None:
    print("无法读取图像，请检查文件路径。")
else:
    # 获取图像大小及灰度平均值
    (height, width, channels), gray = img.shape, cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # print(f"图像大小: 宽 = {width}, 高 = {height}, 通道数 = {channels}")
    print("宽:"+str(width),"高:"+str(height),"通道数:"+str(channels)+"\n灰度平均值: "+str(np.mean(gray)))

    # 获取图像中心的颜色值
    center_pixel = img[height//2 - 1 : height//2 + 1, width//2 - 1 : width//2 + 1]
    print("中心像素颜色 (BGR): \n"+str(center_pixel))

    # 旋转图像并改变图像大小
    rotation_matrix = cv2.getRotationMatrix2D((width // 2, height // 2), 45, 1.0)
    rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))
    resized_img = cv2.resize(img, (width // 2, height // 2))

    # 显示处理后的图像（如需要）
    # cv2.imshow("Rotated Image", rotated_img)
    # cv2.imshow("Resized Image", resized_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
