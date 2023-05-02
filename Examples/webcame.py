import cv2
#pip install opencv-python

cap = cv2.VideoCapture();

while True:
    ret, frame = cap.read()
    
    cv2.imshow("Web Camera",frame)
    
    if cv2.waitKey(1) & 0xFF  == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()