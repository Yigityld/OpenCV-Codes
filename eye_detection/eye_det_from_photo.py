import cv2


img1 = cv2.imread("eye.png")

face_cascade = cv2.CascadeClassifier("frontalface.xml")
eye_cascade = cv2.CascadeClassifier("eye.xml")
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    cv2.rectangle(img1, (x, y), (x+w,y+h), (0, 0, 255), 3)
img2 = img1[y:y+h, x:x+w]
gray1 = gray[y:y+h, x:x+w]
eyes = eye_cascade.detectMultiScale(gray1)
for (ex,ey,ew,eh) in eyes:
    cv2.rectangle(img2, (ex, ey), (ex+ew,ey+eh), (255, 0, 255), 3)
cv2.imshow("original", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()