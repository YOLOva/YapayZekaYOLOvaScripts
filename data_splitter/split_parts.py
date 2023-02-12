

import os
from pathlib import Path
import shutil


dataset_folder=r"D:\Teknofest\YOLOVA\Veriseti\Temizlenenler\Visdrone2019-Det"
split_count=90
prefix="Visdrone2019-Det"
count=0
partnumber=1
for img_path in list(Path(dataset_folder).glob("**/*.jpg")):
    part_folder=os.path.join(dataset_folder, f"{prefix}_part{partnumber}")

    txt_path=str(img_path).replace("\\", "/").replace("/images/", "/labels/").replace(".jpg", ".txt")
    img_copy_dest=os.path.join(part_folder, "images", Path(img_path).name)
    txt_copy_dest=os.path.join(part_folder, "labels", Path(txt_path).name)

    Path(os.path.join(part_folder, "images")).mkdir(parents=True, exist_ok=True)
    Path(os.path.join(part_folder, "labels")).mkdir(parents=True, exist_ok=True)

    shutil.copyfile(img_path, img_copy_dest)
    shutil.copyfile(txt_path, txt_copy_dest)
    count+=1
    if count==split_count:
        count=0
        partnumber+=1
    
