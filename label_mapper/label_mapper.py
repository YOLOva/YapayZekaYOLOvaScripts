
import os
from pathlib import Path
import sys


if len(sys.argv) < 2:
    print("eksik parametre")
    exit()

labels_folder = sys.argv[1]  # "D:/Teknofest/YOLOVA/Veriseti/Visdrone2019Det"
if not Path(labels_folder).is_dir():
    print("hatalı dizin")
    exit()
"""labels_folder = "D:/Teknofest/YOLOVA/Veriseti/New/spat_data/labels_old" #input
output_folder = "D:/Teknofest/YOLOVA/Veriseti/New/spat_data/labels" #output"""
label_map_file = "./label_map_uyz_2023.txt"

# txt dosyasından map listesi çeker
with open(label_map_file, "r") as file:
    lines = file.readlines()

class_map = []
for line in lines:
    class_map.append(line.split()[0])
print(class_map)

# label dosyalarını okuyup sınıflarını mape göre değiştirir
labels_file_names = os.listdir(labels_folder)
for label_file_name in labels_file_names:
    if label_file_name == 'classes.txt':
        continue
    label_path = f"{labels_folder}/{label_file_name}"
    lines = []
    with open(label_path, "r") as label_file:
        data = label_file.readlines()
        for i, line in enumerate(data):
            cls = line.split()[0]
            if class_map[int(cls)] == "-1":
                continue
            lines.append(line.replace(cls, class_map[int(cls)], 1))
    output_folder = labels_folder+"_new"

    Path(labels_folder+"_new").mkdir(exist_ok=True)
    with open(f"{output_folder}/{label_file_name}", 'w') as file:
        file.writelines(lines)
