import cv2
from cvzone.PoseModule import PoseDetector
import socket

cap = cv2.VideoCapture(0)

detector = PoseDetector()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5052)
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img)
##    cv2.imshow("Image",img)
  #  cv2.waitKey(1)
    data=[]
    for lm in lmList:
        data.extend(([lm[0], img.shape[0] - lm[1], lm[2]]))    
    
    sock.sendto(str.encode(str(data)), serverAddressPort)

    

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('s'):
        with open("AnimationFile.txt", 'w') as f:
            f.writelines(["%s\n" % item for item in posList])