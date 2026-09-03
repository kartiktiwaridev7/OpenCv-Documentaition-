import cv2 

image_path = input(" Enter your exact Image location:\n")
image = cv2.imread(image_path)

if image is not None:
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Your Image",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    filename = input("Enter the image name (e.g. output.png): ")
    cv2.imwrite(filename , gray)


else:
    print("Your Image is not loded properly please try again")
