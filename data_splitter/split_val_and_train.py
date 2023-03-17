import os
from pathlib import Path
from random import shuffle
import shutil

def rreplace(string, old, new):
  return new.join(str(string).rsplit(old))

def copyfile(path, dest):
    Path(dest).parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(path, dest)

dataset=r"D:\Teknofest\YOLOVA\Veriseti\KontrolEdildi\Normal\Normal"
output=r"D:\Teknofest\YOLOVA\Veriseti\KontrolEdildi\Normal\Splitted_Train_Val"
all_images_folders=list(Path(dataset).glob("**/images"))

for images_folder_path in all_images_folders:

    def get_dest(path, key, typ):
        return rreplace(str(path).replace(dataset, output).replace("\\", "/"), f"/images/", f"/{key}/{typ}/")
    
    all_images=list(Path(images_folder_path).glob("**/*.jpg"))
    shuffle(all_images)
    num_img=len(all_images)
    local_path=str(images_folder_path).replace(str(images_folder_path.parent.parent), "")
    print("num_img", num_img)
    for i, img_path in enumerate(all_images):
        label_path=rreplace(rreplace(str(img_path).replace("\\", "/"), "/images/", "/labels/"), ".jpg", ".txt")
        if i<num_img*0.8:
           key="train"
        else:
           key="val"
        img_destination= get_dest(img_path, key, "images")
        lbl_destination=rreplace(get_dest(img_path, key, "labels"), ".jpg", ".txt")
        print(lbl_destination)
        copyfile(img_path, img_destination)

        if os.path.exists(label_path):
            copyfile(label_path, lbl_destination)
        
        