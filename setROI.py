import tkinter as tk
import cv2
import numpy as np
import pandas as pd
from tkinter import messagebox
import os

class ROI_setting:
    def messege(self):
        set_windows = tk.Tk()
        set_windows.withdraw()
        messagebox.showinfo('hint', 'chose point and click on the screem clockwisly to set an ROI sample,after those steps,please confirm in the terminal.')
    
    def getfirstframe(self, source):
        cap = cv2.VideoCapture(source)   
        cap.set(cv2.CAP_PROP_POS_FRAMES,1)
        ret, frame = cap.read()
        return frame


    def setROIpoint(self,img):
        

        point_listx, point_listy = [],[]
        def on_EVENT_LBUTTONDOWN(event, x, y, flags,param):

            if event == cv2.EVENT_LBUTTONDOWN:
                xy = "%d,%d" % (x, y)
                point_listx.append(x)
                point_listy.append(y)
                cv2.circle(img, (x, y), 5, (255, 0, 0), thickness=-1)
                cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                            1.0, (0, 0, 0), thickness=3)
                cv2.imshow("image", img)
    

        cv2.namedWindow("image")
        cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
        cv2.imshow("image", img)
        cv2.waitKey(0)

        point_list = list(zip(point_listx,point_listy))


        
        return point_list
    
def save_point_list(point_list, file_path):
    with open(file_path, 'w') as f:
        f.write(str(point_list))  


def getROI(video_path):
    method = ROI_setting()

    frame = method.getfirstframe(video_path)

    method.messege()
    input_ = 'n'
    while input_ == 'n':
        img_ROI = frame.copy()
        point_list = method.setROIpoint(img_ROI)
        input_ = input("confirm ROI:[y] / [n]:")


    return point_list


video_folder = 'video'
roi_id_folder = 'roi_id' 

# read all video files in the video folder
video_files = [f for f in os.listdir(video_folder) if f.endswith('.mp4') or f.endswith('.avi')]
for video_file in video_files:
    video_path = os.path.join(video_folder, video_file)  # select the video file
    
    # Get the video file name without extension
    video_basename = os.path.basename(video_path)  
    video_name = os.path.splitext(video_basename)[0]  
    
    # Create the .txt file path using the video file name
    txt_file_path = os.path.join(roi_id_folder, f"{video_name}.txt")
    
    point_list = getROI(video_path)

    save_point_list(point_list, txt_file_path)
    
    print(f"ROI for {video_file} saved to {txt_file_path}")






