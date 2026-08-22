import cv2

image = cv2.imread(r'C:\Users\dell\Desktop\Open CV\ChatGPT Image Aug 5, 2026, 06_56_32 PM.png')
cropped = image[100:200 , 50:150 ]

cv2.imshow("Original", image)
cv2.imshow("Cropped" , cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()