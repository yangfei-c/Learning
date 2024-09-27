import cv2
import numpy as np

img=cv2.imread("../../img/ChenYao3.webp")
if img is None:
    print("未检出到图像请检查路径是否正确")
else:
    h,w=img.shape[:2]
    pos1 = np.float32([[50, 50], [200, 50], [50, 200]])
    #通常三个点对应左上角，右上角，右下角
    pos2 = np.float32([[10, 100], [200, 50], [100, 250]])

    matrix=cv2.getAffineTransform(pos1,pos2)
    img_affine=cv2.warpAffine(img,matrix,(w,h))
    cv2.imshow("origin",img)
    cv2.imshow("img_affine",img_affine)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

