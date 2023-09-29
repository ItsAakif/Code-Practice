import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Set camera dimensions
wCam, hCam = 640, 480

# Create an instance of the hand detection module
detector = htm.HandDetector()

# Minimum and maximum volume levels
minVol = 0  # Minimum volume
maxVol = 100  # Maximum volume

# Initialize the camera capture
cap = cv2.VideoCapture(0)  # Change the argument to your desired camera index

while True:
    success, img = cap.read()  # Read a frame from the camera
    img = detector.findHands(img)  # Detect hands in the frame
    lmList = detector.findPosition(img, draw=False)  # Find landmarks in the detected hands

    if lmList:
        # Calculate the length between two landmarks (x1, y1) and (x2, y2)
        x1, y1 = lmList[4][1], lmList[4][2]  # Index finger tip
        x2, y2 = lmList[8][1], lmList[8][2]  # Thumb tip
        length = math.hypot(x2 - x1, y2 - y1)

        # Map the length to the volume range
        vol = np.interp(length, [50, 300], [minVol, maxVol])

        # Map the length to control volume bar
        volBar = np.interp(length, [50, 300], [400, 150])

        # Map the length to control volume percentage
        volper = np.interp(length, [50, 300], [0, 100])

        # Print the length and volume
        print(f"Hand length: {int(length)} Volume: {int(vol)}")

        # Set the system volume level
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevelScalar(vol / maxVol, None)

        if length > 50:
            cv2.circle(img, (x1, y1), 15, (0, 255, 0), cv2.FILLED)  # Draw a filled circle on the hand

    # Display the image with volume control information
    cv2.imshow("Hand Gesture Volume Control", img)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
# <HandGestures> by Moutasim Qazi