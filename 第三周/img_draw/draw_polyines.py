import cv2
import numpy as np
img=np.zeros((256,256,3),np.uint8)
h,w,channels=img.shape
pts=np.array([[h//2,w//2],[h//2-30,w//2-30],[h//2+10,w//2+10],[200,15]])
cv2.polylines(img,[pts],True,(155,115,155),3)
# cv2.circle(img,(h//4,w//4),10,(155,115,155),-1,cv2.LINE_4)#-1绘制一个填充的园
cv2.imshow("polylines",img)
cv2.waitKey(0)
cv2.destroyAllWindows()