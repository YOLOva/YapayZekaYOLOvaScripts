
import os
from pathlib import Path


dataset=r"D:\Teknofest\YOLOVA\Veriseti\KontrolEdildi\No_UAIP\Splitted_Train_Val"
def get_local_path(path):
   return str(path).replace(dataset, ".").replace("\\", "/")

trains= [get_local_path(x) for x in list(Path(dataset).glob("**/train"))]
vals=[get_local_path(x) for x in list(Path(dataset).glob("**/val"))]
output_name = "train_dataset.yaml"

with open(os.path.join(dataset, "classes.txt"), "r") as file:
  classes = [line.strip() for line in file.readlines()]

datasetInfo = f"""

train: {trains}

val: {vals}

# test:  images/test

# Classes
nc: {len(classes)}  # number of classes

names: {classes}  # class names
"""
print(datasetInfo)
with open(os.path.join(dataset,output_name), 'w') as f:
    f.write(datasetInfo)