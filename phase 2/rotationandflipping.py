import cv2

image = cv2.imread(r'C:\Users\dell\Desktop\Open CV\ChatGPT Image Aug 5, 2026, 06_56_32 PM.png')

(h,w) = image.shape[:2]
center = (w//2 , h//2)

m = cv2.getRotationMatrix2D(center , 90 ,1.0)
rotated = cv2.warpAffine(image,m,(w,h))

cv2.imshow("Original" , image)
cv2.imshow("Rotated 90 degree " , rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()