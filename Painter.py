import cv2
import numpy as np
import os
import HandTrackingModule as hand # TODO: import the hand tracking module separately from its own folder


# define the Video input
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # sets the webcam width
cap.set(4, 720)  # sets the webcam height

# import the top banner images
headerPaths = os.listdir("headers")
headers = []
for path in headerPaths:
    header = cv2.imread(f"headers/{path}")
    headers.append(header)
currentHeader = headers[0]

# set up the color selection
currentColor = (0, 0, 255)  # default is red
markerSize = 15

# set up the hand detector
detector = hand.handDetector(detectionConfidence=0.85)


while True:

    # load in the video and initialize headers
    success, img = cap.read()
    img = cv2.flip(img,1)

    # use the detector to find the hands and position details
    img = detector.findHands(img)
    landmarks = detector.findPosition(img, draw=False)

    # control flow for the fingers
    if len(landmarks) > 0:
        indexX = landmarks[8][1]
        indexY = landmarks[8][2]
        middleX = landmarks[12][1]
        middleY = landmarks[12][2]
        cv2.circle(img, (indexX, indexY), markerSize, currentColor, cv2.FILLED)
        cv2.putText(img, f'{str(int(indexX))}', (indexX, indexY), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)


        distance = (((middleX - indexX) ** 2) + ((middleY - indexY) ** 2)) ** 0.5
        #cv2.putText(img, f'{str(int(distance))}', (indexX, indexY), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

        # selecting the color
        if indexY < 120:
            if indexX >= 425 and indexX <= 530:
                currentHeader = headers[0]  # red
                currentColor = (0, 0, 255)
                markerSize = 15
            if indexX >= 575 and indexX <= 680:
                currentHeader = headers[1]  # green
                currentColor = (0, 255, 0)
                markerSize = 15
            if indexX >= 730 and indexX <= 840:
                currentHeader = headers[2]  # blue
                currentColor = (255, 0, 0)
                markerSize = 15
            if indexX >= 915 and indexX <= 1020:
                currentHeader = headers[3]  # eraser
                currentColor = (0, 0, 0)
                markerSize = 40
            
            
            


    # display the video output
    img[0:122, 0:1280] = currentHeader
    cv2.imshow("image", img)
    cv2.waitKey(1)

