import cv2
import numpy as np
img=np.zeros((256,256,3),np.uint8)
h,w,channels=img.shape
cv2.rectangle(img,(h//2-50,w//2-50),(h//2+50,w//2+50),(155,115,155),5,cv2.LINE_4)
cv2.imshow("rectangle",img)
cv2.waitKey(0)
cv2.destroyAllWindows()