import os
import cv2
from pathlib import Path
videos_path = "./videos"
save_folder = "./pictures"

for video_path in os.listdir(videos_path):
    try:
        video_path = f"{videos_path}/{video_path}" # video klasörü
        vidcap = cv2.VideoCapture(video_path) # video yakalanır
        success, image = vidcap.read() #her readte bir resim alınır
        video_name = Path(video_path).stem # video ismi alınır kaydetmek için
        count = 0 # sayıcı
        video_save_folder = f"{save_folder}/{video_name}" # resimleri kaydetme klasörü
        Path(video_save_folder).mkdir(exist_ok=True) # kaydedilecek klasör yoksa oluşturur.
        while success: # resimleri bitene kadar devam eder
            # görsel kaydedilir.
            cv2.imwrite(f"{video_save_folder}/{video_name}_{count}.jpg", 
                        image)     # save frame as JPEG file
            #sonraki görsel okunur.
            success, image = vidcap.read()
            print('Read a new frame: ', success)
            count += 1
    except: 
        print("Hata")
