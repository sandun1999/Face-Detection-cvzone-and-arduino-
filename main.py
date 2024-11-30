import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject

cap = cv2.VideoCapture(0)
detector = FaceDetector()
arduino = SerialObject('COM3')

while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img)

    if bboxs:
        arduino.sendData([1, 0])
    else:
        arduino.sendData([0, 1])

    # Display the image in a window named 'Image'
    cv2.imshow("Image", img)
    # Wait for 1 millisecond, and keep the window open
    cv2.waitKey(1)
