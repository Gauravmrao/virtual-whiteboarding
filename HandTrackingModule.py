import cv2
import mediapipe as mp
import time

class handDetector():

    # initialize the class
    def __init__(self, mode = False, maxHands = 2, modelComplexity = 1, detectionConfidence = 0.5, trackingConfidence = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplexity = modelComplexity
        self.detectionConfidence = detectionConfidence
        self.trackingConfidence = trackingConfidence
        
        # initialize the hand tracker objects
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplexity, self.detectionConfidence, self.trackingConfidence)
        self.mpDraw = mp.solutions.drawing_utils


    # find and draw the hands from video
    def findHands(self, img, draw = True):
        
        # hands object needs RGB, so convert input
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
        self.results = self.hands.process(imgRGB)

        # display the detection for each hand in frame
        if self.results.multi_hand_landmarks:
            for handLandmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLandmarks, self.mpHands.HAND_CONNECTIONS)
        return img
    

    # return a list of all of the landmark positions
    def findPosition(self, img, handNumber = 0, draw = True):
        landmarkList = []

        # get the data for each individual landmark and corresponding id
        if self.results.multi_hand_landmarks:  
            currHand = self.results.multi_hand_landmarks[handNumber]
            for id, landmark in enumerate(currHand.landmark):
                height, width, channels = img.shape
                centerX = int(landmark.x * width)
                centerY = int(landmark.y * height)
                landmarkList.append([id, centerX, centerY])
                if draw:
                    cv2.putText(img, str(id), (centerX, centerY), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 1)
        return landmarkList



def main():
    
    # initialize objects and variables
    cap = cv2.VideoCapture(0)
    prevTime = 0
    currTime = 0
    detector = handDetector()

    # start running the webcam
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        landmarkList = detector.findPosition(img)
        if len(landmarkList) != 0:
            print(landmarkList[8])

        # calculate and display the FPS
        currTime = time.time()
        fps = 1/(currTime - prevTime)
        prevTime = currTime

        # display the webcam - output
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 0), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()