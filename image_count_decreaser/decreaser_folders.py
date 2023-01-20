import os
import shutil
from pathlib import Path

reduce_folders = r"D:\Teknofest\YOLOVA\Veriseti\UYZ2022"
for f_name in os.listdir(reduce_folders):
    reduce_folder = os.path.join(
        reduce_folders, f_name, "images").replace("\\", "/")
    save_folder = reduce_folder.replace("/UYZ2022/", "/UYZ2022_Azaltildi/")
    reduced_list = sorted(os.listdir(reduce_folder))
    for i in range(4):
        reduced_list = [x for index, x in enumerate(
            reduced_list) if index % 2 == 0]
    for image_name in reduced_list:
        Path(save_folder.replace("/images", "/labels")
             ).mkdir(exist_ok=True, parents=True)
        Path(save_folder).mkdir(exist_ok=True, parents=True)
        shutil.copy(reduce_folder.replace("/images", "/labels")+ "/"+ Path(image_name).stem+".txt",
                        save_folder.replace("/images", "/labels") + "/"+ Path(image_name).stem+".txt")
        shutil.copy(os.path.join(reduce_folder, image_name),
                        os.path.join(save_folder, image_name))
