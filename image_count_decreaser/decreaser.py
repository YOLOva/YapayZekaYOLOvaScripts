import os
import shutil
from pathlib import Path
reduce_folder = r"D:\Teknofest\YOLOVA\Veriseti\video\asonra\pedestrians"
save_folder = f"{reduce_folder}_azaltildi"
reduced_list = sorted(os.listdir(reduce_folder+"/images"))
for i in range(2):
  reduced_list = [x for index, x in enumerate(reduced_list) if index%2==0]
for image_name  in reduced_list:
  Path(save_folder+"/labels/").mkdir(exist_ok=True, parents=True)
  Path(save_folder+"/images/").mkdir(exist_ok=True, parents=True)
  try:
    shutil.copy(reduce_folder+"/labels/"+Path(image_name).stem+".txt", save_folder+"/labels/"+Path(image_name).stem+".txt")
    shutil.copy(reduce_folder+"/images/"+image_name, save_folder+"/images/"+image_name)
  except:
    pass
