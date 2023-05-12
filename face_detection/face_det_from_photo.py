import cv2


img1 = cv2.imread("face.png")

face_cascade = cv2.CascadeClassifier("frontalface (1).xml")

gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 7)

for (x,y,w,h) in faces:
    cv2.rectangle(img1, (x, y), (x+w,y+h), (0, 0, 255), 2)

cv2.imshow("original", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


