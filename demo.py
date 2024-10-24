import cv2
import numpy as np
from vUtils.capture import DeVibVideoCapture, VibrationCalibrator
from vUtils.player import Player

baseImg = cv2.imread("base/base.png")
mtx, dist = np.load("base/undistort.npy", allow_pickle=True)
baseImg = cv2.undistort(baseImg, mtx, dist)
calibrator = VibrationCalibrator(baseImg=baseImg)
cap = DeVibVideoCapture(
    videoPath="video/demo.mp4",
    initStep=0,         # Initial frame step (if applicable)
    interval=50,        # Interval for reading
    mtx=mtx,
    dist=dist,
    calibrator=calibrator,
)
player = Player()

while True:
    ret, img = cap.read()
    if ret:
        player.show(img)
    else:
        exit()
