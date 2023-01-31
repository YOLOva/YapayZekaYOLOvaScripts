import os
from pathlib import Path
import shutil
import sys
from os.path import exists
if len(sys.argv)<2:
    print("eksik parametre")
    exit()

dataset_dir = sys.argv[1]  # "D:/Teknofest/YOLOVA/Veriseti/Visdrone2019Det"
if not Path(dataset_dir).is_dir():
    print("hatalı dizin")
    exit()

labels_dir = f"{dataset_dir}/labels"
images_dir = f"{dataset_dir}/images"
unlabelled_dir = f"{dataset_dir}/unlabelled_dir"
picture_not_found = f"{dataset_dir}/picture_not_found"


look_to_clean = [[labels_dir, images_dir, "txt", "jpg", picture_not_found],  # resimsiz labeller
                 [images_dir, labels_dir, "jpg", "txt", unlabelled_dir]]  # labelsiz resimler


for lc in look_to_clean:
    cl_list = os.listdir(lc[0])
    for cl_name in cl_list:
        if cl_name == 'classes.txt':
            continue
        look_path = f"{lc[1]}/{Path(cl_name).stem}.{lc[3]}"
        cl_path = f"{lc[0]}/{cl_name}"
        if not exists(look_path):
            Path(lc[4]).mkdir(parents=True, exist_ok=True)
            shutil.move(cl_path, f"{lc[4]}/{cl_name}")
