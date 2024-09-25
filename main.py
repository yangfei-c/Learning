import cv2

img=cv2.imread("img/ChenYao3.webp")
#./表示openv/
#img/，img要和main.py同一个路径
cv2.imshow("Chen Yao",img)#不支持非ASCII码
k=cv2.waitKey(7000)
#参数为0表示一直，参数大于0表示等待多少毫秒
#同时看键盘是否有输入会返回一个ASCII值
if k==27:
    cv2.destroyAllWindows()
