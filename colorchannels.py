import cv2  # OpenCv Import 

image = cv2.imread(r'C:\Users\dell\Desktop\Open CV\ChatGPT Image Aug 5, 2026, 06_56_32 PM.png')

if image is not None: 
    h,w,c = image.shape
    print(f" image loded : \n Height{h} : \n Width{w} \n Channels:{c}")

else:
    print("Could not load Image")