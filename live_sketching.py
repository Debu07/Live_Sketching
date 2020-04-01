#import keras
import cv2
#import numpy as np
#import matplotlib
print (cv2.__version__)

# Our sketch generating function
def sketch(image):
    # Convert image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Clean up image using Guassian Blur
    img_gray_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)

    # Extract edges
    #instead of canny two other functions are Sobel and Laplacian Canny is optimaland has low error rate
    canny_edges = cv2.Canny(img_gray_blur, 20, 50)

    # Do an invert binarize the image
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask


# Initialize webcam, cap is the object provided by VideoCapture
# It contains a boolean indicating if it was sucessful (ret)
# It also contains the images collected from the webcam (frame)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Our Live Sketcher', sketch(frame))
    if cv2.waitKey(1)==ord('c'):
        cv2.imwrite(filename="sketch.jpg",img=sketch(frame))
        cv2.imwrite(filename="original.jpg",img=frame)
        cap.release()
        cv2.destroyAllWindows()
    elif cv2.waitKey(1) == 13:  # 13 is the Enter Key
        break

# Release camera and close windows
cap.release()
cv2.destroyAllWindows()
