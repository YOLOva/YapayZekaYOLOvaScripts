import os
from pathlib import Path
import re  

files_path = r"D:\Teknofest\YOLOVA\Veriseti\frame_devrim_last_azaltildi\labels"
for file_path in list(Path(files_path).glob("**/*.jpg")):
    file_path=str(file_path)
    reg=r"\.rf.+"
    new_file_path= re.sub(reg, "", file_path).replace(".jpg", ".txt")
    Path(file_path).rename(new_file_path)