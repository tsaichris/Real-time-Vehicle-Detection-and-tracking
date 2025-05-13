import cv2
from utlis import getROI
import os

# get the frame
video_path = 'video\\33.mp4'
roi_id_folder = 'roi_id'
cap = cv2.VideoCapture(video_path)   
cap.set(cv2.CAP_PROP_POS_FRAMES,1)
ret, frame = cap.read()

frame_ROI = getROI(frame, video_path, roi_id_folder)
cv2.imshow('ROI', frame_ROI)
cv2.waitKey(0)
cv2.imwrite('roi_frame.png', frame_ROI)