# Virtual Paint Application

## Project Overview
This project is a **Virtual Paint Application** using a webcam and hand tracking technology. The user can select colors, draw on a canvas, and erase sections by interacting with a virtual interface. The core functionality is implemented using OpenCV for image processing and a custom hand tracking module for gesture detection.

## Features
- **Hand Gesture Recognition**: Detects hand gestures using the index and middle fingers to switch between drawing mode and color selection mode.
- **Drawing Interface**: Draws lines or circles on the canvas in different colors based on user input.
- **Color Selection**: Choose between multiple colors (Red, Green, Blue) or switch to an eraser via hand gestures.
- **Real-time Interaction**: Displays the drawing canvas in real-time, merging the webcam feed and the virtual canvas.

## Installation and Activation
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
