import cv2
#cv2.CAPD_show yazarsan kırmızı hata kalkar
cap = cv2.VideoCapture("antalya.mp4")
# cap =cv2.VideoCapture(0) = webcam

while True:
    ret, frame = cap.read()
    if ret == 0:
        break
        #video bitince çıkarır
    frame = cv2.flip(frame, 1)
    cv2.imshow("Antalya", frame)
    #eğer webcamse üste webcam yaz
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
