import os
from pathlib import Path
import re  

files_path = r"D:\Teknofest\YOLOVA\Veriseti\VEDAI\images"
for file_path in list(Path(files_path).glob("**/*.jpg")):
    file_path=str(file_path)
    new_file_path= file_path.replace("_co.jpg", ".jpg")
    Path(file_path).rename(new_file_path)