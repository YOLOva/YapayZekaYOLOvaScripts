
import os
from pathlib import Path
import sys
import argparse

def run(
        labels_folder="",
        output_folder="",
        label_map_file="./label_map_uyz_2023.txt",
        ):

    if labels_folder == '':
        print("labels_folder parametresi eksik.")
        exit()

    if not Path(labels_folder).is_dir():
        print("hatalı labels_folder dizin")
        exit()

    Path(output_folder).mkdir(exist_ok=True, parents=True)
    if output_folder == "":
        output_folder = labels_folder+"_new"
        
    elif not Path(output_folder).is_dir():
        print("hatalı output_folder dizin")
        exit()
    
    if not Path(label_map_file).is_file():
        print("hatalı label_map_file dizin")
        exit()

    # txt dosyasından map listesi çeker
    with open(label_map_file, "r") as file:
        lines = file.readlines()
    
    Path(output_folder).mkdir(exist_ok=True)

    class_map = []
    for line in lines:
        class_map.append(line.split()[0])
    print(class_map)

    # label dosyalarını okuyup sınıflarını mape göre değiştirir
    labels_file_names = os.listdir(labels_folder)
    for label_file_name in labels_file_names:
        if label_file_name == 'classes.txt':
            continue
        label_path = f"{labels_folder}/{label_file_name}"
        lines = []
        with open(label_path, "r") as label_file:
            data = label_file.readlines()
            for i, line in enumerate(data):
                cls = line.split()[0]
                if class_map[int(cls)] == "-1":
                    continue
                lines.append(line.replace(cls, class_map[int(cls)], 1))

        with open(f"{output_folder}/{label_file_name}", 'w') as file:
            file.writelines(lines)



def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--labels-folder', type=str, help='label klasörü dizini', required=True)
    parser.add_argument('--output-folder', default="", type=str, help='çıktı klasör dizini')
    parser.add_argument('--label-map-file', type=str, default="./label_map_uyz_2023.txt")
    opt = parser.parse_args()
    return opt

def main(opt):
    run(**vars(opt))


if __name__ == "__main__":
    opt = parse_opt()
    main(opt)