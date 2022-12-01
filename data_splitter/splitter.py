import os
from pathlib import Path
import shutil

dataset_folder = "D:/Teknofest/YOLOVA/Veriseti/VAID_dataset-20221119T115100Z-003/VAID_dataset/cleared"
part_dest = "/parts"
n_part = 2

images_folder = dataset_folder+"/images/"
image_names = os.listdir(images_folder)
part_len = len(image_names)/n_part
for i in range(n_part):
    start = i*part_len
    end = (i+1)*part_len
    for image_name in image_names[int(start):int(end)]:
        label_name = Path(image_name).stem+".txt"
        image_path = images_folder+image_name
        label_path = images_folder.replace(
            "/images/", "/labels/") + label_name

        p_d_l = label_path.replace(
            dataset_folder, dataset_folder+f"{part_dest}/{i}")
        p_d_i = image_path.replace(
            dataset_folder, dataset_folder+f"{part_dest}/{i}")
        Path(p_d_l.replace(label_name, "")).mkdir(parents=True, exist_ok=True)
        Path(p_d_i.replace(image_name, "")).mkdir(parents=True, exist_ok=True)
        shutil.copyfile(label_path, p_d_l)
        shutil.copyfile(image_path, p_d_i)
