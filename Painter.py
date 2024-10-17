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
prevPoint = (-1, -1)

# set up the hand detector
detector = hand.handDetector(detectionConfidence=0.85)
imgCanvas = np.zeros((720, 1280, 3), np.uint8)


while True:

    # load in the video and initialize headers
    success, img = cap.read()
    img = cv2.flip(img,1)

    # use the detector to find the hands and position details
    img = detector.findHands(img)
    landmarks = detector.findPosition(img, draw=False)

    # control flow for the fingers
    if len(landmarks) > 0:

        # finger tips
        indexX = landmarks[8][1]
        indexY = landmarks[8][2]
        middleX = landmarks[12][1]
        middleY = landmarks[12][2]
        #cv2.putText(img, f'{str(int(indexX))}', (indexX, indexY), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

        # knuckles
        indKnuckleX = landmarks[6][1]
        indKnuckleY = landmarks[6][2]
        midKnuckleX = landmarks[10][1]
        midKnuckleY = landmarks[10][2]


        """ 
        calculate the cross product of the index and middle fingertips
        this will allow us to check if both fingers are raised, or in this case,
        if both fingertips are on the same side of the vector created by the line
        segment between the two knuckles. This can be used for changing the modes 
        between drawing and color selection.
        """

        # Calculate the cross product of two 2D vectors v1 and v2
        def cross_product(v1, v2):
            return v1[0] * v2[1] - v1[1] * v2[0]

        # Check if points P and Q are on the same side of the line created by the segment AB.
        def sameSide(A, B, P, Q):
            # Vector AB
            AB = (B[0] - A[0], B[1] - A[1])
            # Vector AP and AQ
            AP = (P[0] - A[0], P[1] - A[1])
            AQ = (Q[0] - A[0], Q[1] - A[1])
            # Cross products
            cross1 = cross_product(AB, AP)
            cross2 = cross_product(AB, AQ)
            # Check if the cross products have the same sign
            return cross1 * cross2 >= 0  # Same side if the signs are the same


        # color selection mode - selecting the color
        if sameSide((indKnuckleX, indKnuckleY), (midKnuckleX, midKnuckleY), (indexX, indexY), (middleX, middleY)):
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
            cv2.circle(img, (indexX, indexY), markerSize, currentColor, 5)
            prevPoint = (indexX, indexY)
        
        # drawing mode
        else:
            cv2.circle(img, (indexX, indexY), markerSize, currentColor, cv2.FILLED)

            # the program has just begun
            if prevPoint == (-1, -1):
                prevPoint = (indexX, indexY)


            cv2.line(img, prevPoint, (indexX, indexY), currentColor, markerSize)
            cv2.line(imgCanvas, prevPoint, (indexX, indexY), currentColor, markerSize)
            prevPoint = (indexX, indexY)


        

        
            
    # overlay the drawing canvas onto the video output
    imgGrey = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY) 
    _, imgInv = cv2.threshold(imgGrey, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)
            


    # display the video output
    img[0:122, 0:1280] = currentHeader
    cv2.imshow("image", img)
    cv2.waitKey(1)

