import cv2

image = cv2.imread(r'C:\Users\dell\Desktop\Open CV\ChatGPT Image Aug 5, 2026, 06_56_32 PM.png')

if image is not None:
    gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale image " ,gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Could not load the image please re check you img location")
