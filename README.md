# Virtual Whiteboarding with Computer Vision

## Project Overview
This project is a **Virtual Whiteboarding** application using a webcam and hand tracking technology. The user can select colors, draw on a canvas, and erase sections by interacting with a virtual interface. The core functionality is implemented using OpenCV for image processing and Mediapipe for gesture detection.


## Features
- **Hand Gesture Recognition**: Detects hand gestures using the index and middle fingers to switch between drawing mode and color selection mode.
- **Drawing Interface**: Draws lines or circles on the canvas in different colors based on user input.
- **Color Selection**: Choose between multiple colors (Red, Green, Blue) or switch to an eraser via hand gestures.
- **Real-time Interaction**: Displays the drawing canvas in real-time, merging the webcam feed and the virtual canvas.


## How to install and run the project
**Note:** This program requires a working webcam.

1. Clone the repository and navigate to the associated directory:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
2. Install the required Python Packages
    ```bash
    pip install -r requirements.txt
3. Run the Python Script
   ```bash
    python virtual_paint.py


## How to Use
- Hold your index and middle fingers up to enter *selection* mode. In this state, you will be able to select your marker color by moving your fingers together to the desired color at the top of the screen.
- By putting your middle finger down, you will enter *drawing* mode, in which you can draw on the screen in the chosen color using your index finger.
- If you wish to change colors, you will have to enter *selection* mode again and select your new color.
- You can also **erase** from your drawing by selecting the eraser from the top of the screen when in *selection* mode, and then drawing with the eraser over the screen in *drawing* mode.
**Tip:** You can "lift" your marker to stop drawing and begin drawing on another part of the screen by alternating between the *selection* and "drawing* modes.


## Key Python Libraries Used

### 1. **OpenCV** (`cv2`)
OpenCV is one of the most popular libraries for computer vision tasks. It is used here to:
   - Capture video input from the webcam.
   - Process and display the video feed.
   - Draw on the screen  and display visual elements like lines and circles based on user input and hand gestures.

OpenCV was chosen for its versatility in handling real-time video processing and its extensive support for image processing operations.

### 2. **MediaPipe** (`mediapipe`)
MediaPipe is a framework for building multimodal applied machine learning pipelines. It is used in this project via a custom `HandTrackingModule` to:
   - Detect and track hand landmarks in real-time, such as from the tips of the middle and index fingers.
   - Provide high accuracy and efficiency for hand gesture recognition.

MediaPipe was chosen for its state-of-the-art performance in hand tracking and its ability to run efficiently in real-time on various devices.


## Potential Future Extensions

This project can be extended in various ways to add more features and increase its scope of use:

1. **Additional Gesture Controls**
   - Expanding the application to support more complex gestures for additional functionalities, such as changing brush sizes or applying different drawing effects (e.g., shapes, patterns).
2. **Collaboration Features**
   - Enabling multiple users to draw on the same canvas in real-time, promoting collaborative creativity and learning experiences.


## Social Impact

The Hand Gesture Drawing Application has the potential to make a significant social impact by:

1. **Promoting Creativity:** It encourages artistic expression and creativity, allowing users to create art in an interactive and engaging manner, particularly beneficial for children and educational settings.
2. **Enhancing Accessibility:** This application can serve as a therapeutic tool for individuals with disabilities, providing them with a unique way to communicate and express themselves through art.
3. **Whiteboarding Practice:** As whiteboarding increasingly becomes an integral part of the interview process for many companies, this tool can provide an easy and creative way to prepare for interviews.


