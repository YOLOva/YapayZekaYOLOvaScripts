import os
import shutil
from sys import argv

# path = "./images"
if len(argv)<2 or argv[1] == "":
    print("eksik parametre")
    exit()

path = argv[1]
save_path = "./decreased"
fps = 30

image_list = os.listdir(path)
for index, image_path in enumerate(image_list):
    destination = f"{save_path}/{image_path}"
    image_path = f"{path}/{image_path}"
    if(index % fps == 0):
        shutil.copyfile(image_path, destination)
