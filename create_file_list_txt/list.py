import os
import sys

if len(sys.argv)<3:
    print("eksik parametre")




list_dir = "D:/Teknofest/YOLOVA/Veriseti/Visdrone2019-DET-to-uyz/test-dev/images"
output_name = "visdrone_det2019_test-dev"

list = os.listdir(list_dir)

with open(output_name+".txt", "w") as file:
    file.writelines([line + "\n" for line in list])
