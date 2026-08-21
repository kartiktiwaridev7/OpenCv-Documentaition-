import cv2 

image_path = input("Enter you Image path:\n")

image = cv2.imread(image_path)

if image is not None:
    print("Image is loded")
    dim_str = input(" Enter the dimensions of the image (for ex- 300 , 300) First is width and 2nd is Height \n ")

    # Split the string 
    width_str , height_str = dim_str.split()
    dim = (int(width_str), int(height_str))
    resize = cv2.resize(image , dim)
    cv2.imshow("original Image" , image)
    cv2.imshow("resized Image" , resize)
    cv2.imwrite("resize_output.png" , resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
