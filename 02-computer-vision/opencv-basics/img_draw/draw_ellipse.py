import cv2
import numpy as np
img=np.zeros((256,256,3),np.uint8)
h,w,channels=img.shape
cv2.ellipse(img,(h//2,w//2),(100,50),40,0,300,(155,115,155),3,cv2.LINE_4)
# cv2.circle(img,(h//4,w//4),10,(155,115,155),-1,cv2.LINE_4)#-1绘制一个填充的园
cv2.imshow("ellipse",img)
cv2.waitKey(0)
cv2.destroyAllWindows()