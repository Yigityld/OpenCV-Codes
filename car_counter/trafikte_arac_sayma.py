import cv2

cap = cv2.VideoCapture("traffic (1).avi")
font = cv2.FONT_HERSHEY_SIMPLEX
backsub = cv2.createBackgroundSubtractorMOG2()
c = 0
while True:
    ret, frame = cap.read()

    if ret:
        fgmask = backsub.apply(frame)
        cv2.line(frame, (50, 0), (50, 300), (0, 255, 0), 2)
        cv2.line(frame, (70, 0), (70, 300), (0, 255, 0), 2)

        conturs, hiyerarchi = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        try:
            hiyerarchi = hiyerarchi[0]
        except:
            hiyerarchi = []

        for cnt, hier in zip(conturs, hiyerarchi):
            (x, y, h, w) = cv2.boundingRect(cnt)
            if w > 40 and h > 40:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
                if 50 < x < 70:
                    c += 1

        cv2.putText(frame, "car:" + str(c), (90, 100), font, 2, (0, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow("mask", frame)
        cv2.imshow("fgmask", fgmask)
        if cv2.waitKey(40) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
