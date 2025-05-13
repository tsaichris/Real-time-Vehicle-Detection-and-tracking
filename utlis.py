    
import cv2
import numpy as np
import argparse
import os
import time as Time
import ast


def getROI(frame, video_path, roi_id_folder):
    """
    input:
    
    """
    video_basename = os.path.basename(video_path)  
    video_name = os.path.splitext(video_basename)[0]  
  


    txt_file_path = os.path.join(roi_id_folder, f"{video_name}.txt")
    def read_point_list(file_path):
        with open(file_path, 'r') as f:
            content = f.read().strip()
            # Use ast.literal_eval to safely evaluate the string as a Python literal
            point_list = ast.literal_eval(content)
        return point_list

    point_list = read_point_list(txt_file_path)




    #ROI
    trapezoid= np.array([point_list])
    black_image = np.zeros_like(frame)
    mask = cv2.fillPoly(black_image, trapezoid, (255,255,255))
    # applying mask on original image
    frame_roi = cv2.bitwise_and(frame, mask)

    return frame_roi