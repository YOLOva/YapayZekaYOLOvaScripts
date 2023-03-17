
import os
from pathlib import Path
import sys
import argparse

def run(
        labels_folder="",
        label_map_file="./label_map_uyz_2023.txt",
        ):

    if labels_folder == '':
        print("labels_folder parametresi eksik.")
        exit()

    if not Path(labels_folder).is_dir():
        print("hatalı labels_folder dizin")
        exit()
    
    if not Path(label_map_file).is_file():
        print("hatalı label_map_file dizin")
        exit()

    # txt dosyasından map listesi çeker
    with open(label_map_file, "r") as file:
        lines = file.readlines()

    max_cls=max([int(line.split()[0]) for line in lines])
    class_name_map = ["" for i in range(max_cls+1)]
    for line in lines:
        cls, name=line.strip().split()
        class_name_map[int(cls)]=name+"\n"
        
    print(class_name_map)
    print("max", max_cls)

    for label_path in Path(labels_folder).glob("**/classes.txt"):
        with open(label_path, 'w') as file:
            file.writelines(class_name_map)



def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--labels-folder', type=str, help='label klasörü dizini', required=True)
    parser.add_argument('--label-map-file', type=str, default="./label_map_uyz_2023.txt")
    opt = parser.parse_args()
    return opt

def main(opt):
    run(**vars(opt))


if __name__ == "__main__":
    opt = parse_opt()
    main(opt)