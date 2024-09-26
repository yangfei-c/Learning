import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
h,w,channels=img.shape
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'da jia hao',(h//2,w//2),font,2,(255,255,0),2)

cv2.imshow("text",img)
cv2.waitKey(0)
cv2.destroyAllWindows()