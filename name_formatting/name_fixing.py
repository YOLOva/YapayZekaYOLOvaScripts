import os
from pathlib import Path
import re  

files_path = "D:\Teknofest\CATAI\Verisetleri\Visdrone\VisDrone2019\labels"
files_name_list = os.listdir(files_path)
for file_name in files_name_list:
    file_path = f"{files_path}/{file_name}"

    #name process
    new_name = re.sub(r"\d+_(?=((\d+_){2}d_\d+))", "", file_name)
    new_file_path = f"{files_path}/{new_name}"

    #rename
    Path(file_path).rename(new_file_path)