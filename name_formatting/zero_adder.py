import os
from pathlib import Path


name_length = 6
files_folder = "D:/Teknofest/YOLOVA/Veriseti/VAID_dataset-20221119T115100Z-003/VAID_dataset/JPEGImages2/2"
files = os.listdir(files_folder)

for fileWe in files:
    filename = Path(fileWe).stem
    count = name_length-len(filename)
    if count > 0:
        file_old = f"{files_folder}/{fileWe}"
        fileWe = "0"*(name_length-len(filename))+fileWe
        file_new = f"{files_folder}/{fileWe}"
        Path(file_old).rename(file_new)