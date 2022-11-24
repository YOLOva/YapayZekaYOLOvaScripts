import os
import cv2
from pathlib import Path
videos_path = "./videos"
save_folder = "./pictures"
image_per_second = 1

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

for video_path in os.listdir(videos_path):
    try: # video klasöründe video harici bir dosya varsa hata verebilir işlemlerin iptal edilmemesi için try catch
        if video_path == "readme.md":
            continue
        video_path = f"{videos_path}/{video_path}" # video klasörü
        vidcap = cv2.VideoCapture(video_path) # video yakalanır
        if int(major_ver)  < 3 :
            fps = round(vidcap.get(cv2.cv.CV_CAP_PROP_FPS))
            print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
        else :
            fps = round(vidcap.get(cv2.CAP_PROP_FPS))
            print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
        success, image = vidcap.read() #her readte bir resim alınır
        video_name = Path(video_path).stem # video ismi alınır kaydetmek için
        count = 0 # sayıcı
        video_save_folder = f"{save_folder}/{video_name}" # resimleri kaydetme klasörü
        Path(video_save_folder).mkdir(exist_ok=True) # kaydedilecek klasör yoksa oluşturur.
        while success: # resimleri bitene kadar devam eder
            # görsel kaydedilir.
            if(count%round(fps/image_per_second) !=  0):
                cv2.imwrite(f"{video_save_folder}/{video_name}_{count}.jpg", 
                        image)     # save frame as JPEG file
            #sonraki görsel okunur.
            success, image = vidcap.read()
            print('Read a new frame: ', success)
            count += 1
    except: 
        print("Hata")
