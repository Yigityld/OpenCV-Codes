import cv2

cap = cv2.VideoCapture(0)
car_cascade = cv2.CascadeClassifier("car.xml")

while True:
    ret, frame = cap.read()

    frame = cv2.resize(frame, (480, 360))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, 1.1, 2)

    for (x,y,w,h) in cars:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)
    cv2.imshow("mask", frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()