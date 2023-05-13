import cv2

cap = cv2.VideoCapture(0)
smile_cascade = cv2.CascadeClassifier("smile.xml")
face_cascade = cv2.CascadeClassifier("frontalface.xml")
while True:
    ret, frame = cap.read()

    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(frame, 1.5, 9)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        roi_frame = frame[y:y+h, x: x+w]
        roi_gray = gray[y:y+h, x: x+w]
        smiles = smile_cascade.detectMultiScale(roi_frame, 1.5, 9)

        for (ex, ey, ew, eh) in smiles:
            cv2.rectangle(roi_frame, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

    cv2.imshow("mask", frame)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
