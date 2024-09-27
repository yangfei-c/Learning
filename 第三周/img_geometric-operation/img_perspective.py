import cv2
import numpy as np

img=cv2.imread("../../img/A4.png")
if img is None:
    print("未检出到图像请检查路径是否正确")
else:
    h,w=img.shape[:2]
    pos1 = np.float32([[114, 82], [287, 156], [8, 322], [216, 333]])
    pos2 = np.float32([[0, 0], [188, 0], [0, 262], [188, 262]])

    matrix=cv2.getPerspectiveTransform(pos1,pos2)
    img_perspective=cv2.warpPerspective(img,matrix,(190,272))
    cv2.imshow("origin",img)
    cv2.imshow("img_affine",img_perspective)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

