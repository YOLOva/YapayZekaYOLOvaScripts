import os
from pathlib import Path


# centerx centery orientation cls _ _ [Four_Corners]
mapx = {
    1: 0,
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 5,
    7: 6,
    8: 14,
    9: 7,
    10: 8,
    11: 9,
    12: 10,
    13: 11,
    31: 12,
    23: 13
}


def vedai_to_yolo(dir):
    with open(os.path.join(dir, "annotation1024.txt"), "r") as f:
        lines = f.readlines()
        new_lines=[]
        txtname=""
        for index, line in enumerate(lines):
            attrs=line.split()
            current_txt_name=attrs[0]
            if index==0:
                txtname=attrs[0]
            if txtname!=current_txt_name:
                with open(os.path.join(dir, "labels", txtname+".txt"), 'w') as fl:
                    fl.writelines(new_lines)
                new_lines=[]
                txtname=current_txt_name
            cls=mapx[int(attrs[-3])]
            attrs = [float(x) for x in attrs]
            centerx = attrs[1]/1024
            centery = attrs[2]/1024
            cornersx = attrs[4:8]
            cornersy = attrs[8:12]
            minx = min(cornersx)
            miny = min(cornersy)
            maxx = max(cornersx)
            maxy = max(cornersy)
            width = (maxx-minx)/1024
            height = (maxy-miny)/1024
            new_lines.append(
                    f"{cls} {centerx} {centery} {width} {height}\n")
            
                


        


vedai_to_yolo(r"D:\Teknofest\YOLOVA\Veriseti\VEDAI")
