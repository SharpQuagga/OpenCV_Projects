import cv2

cap = cv2.VideoCapture(0)

def sketch(image):
    gray_scale = cv2.cvtColor(image,cv2.IMREAD_GRAYSCALE)
    img_blur = cv2.GaussianBlur(gray_scale,(5,5),0)
    canny_edge = cv2.Canny(img_blur,40,90)
    re,mask = cv2.threshold(canny_edge,70,255,cv2.THRESH_BINARY_INV)

    return mask


while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("frame",sketch(frame))

    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()