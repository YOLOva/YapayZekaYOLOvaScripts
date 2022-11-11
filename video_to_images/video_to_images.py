import os
import cv2
from pathlib import Path
videos_path = "./videos"
save_folder = "./pictures"

for video_path in os.listdir(videos_path):
    try:
        video_path = f"{videos_path}/{video_path}"
        vidcap = cv2.VideoCapture(video_path)
        success, image = vidcap.read()
        video_name = Path(video_path).stem
        count = 0
        video_save_folder = f"{save_folder}/{video_name}"
        Path(video_save_folder).mkdir(exist_ok=True)
        while success:
            cv2.imwrite(f"{video_save_folder}/{video_name}_{count}.jpg",
                        image)     # save frame as JPEG file
            success, image = vidcap.read()
            print('Read a new frame: ', success)
            count += 1
    except: 
        print("Hata")
