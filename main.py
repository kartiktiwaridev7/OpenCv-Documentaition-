import cv2

image  = cv2.imread("ChatGPT Image Aug 5, 2026, 06_56_32 PM.png")

if image is not None: 
    gray = cv2.cutcolor (image , cv2.COLOR_BGR2GRAY)
    cv2.imshow("Image showing" , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print(" Image loded succesfully")



print ("Program is ended ")
