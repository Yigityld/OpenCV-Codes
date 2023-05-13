import cv2


img = cv2.imread("smile.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier("frontalface.xml")
smile_cascade = cv2.CascadeClassifier("smile.xml")
faces = face_cascade.detectMultiScale(gray, 1.6, 9)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x, y), (x+w,y+h), (0, 0, 255), 3)


roi_img = img[y:y+h, x:x+w]
roi_gray = gray[y:y+h, x:x+w]
smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 10)

for (x,y,w,h) in smiles:
    cv2.rectangle(roi_img, (x, y), (x+w,y+h), (0, 255, 0), 3)
cv2.imshow("original", img)

cv2.waitKey(0)
cv2.destroyAllWindows()