import os
from pathlib import Path
import xml.etree.ElementTree as ET
from src.pascalvoc_to_yolo import PascalVOC_to_YOLO

output_folder = "D:/Teknofest/YOLOVA/Veriseti/VAID_dataset-20221119T115100Z-003/VAID_dataset/labels"
pascal_annotations_folder = "D:/Teknofest/YOLOVA/Veriseti/VAID_dataset-20221119T115100Z-003/VAID_dataset/Annotations"
ann_list = os.listdir(pascal_annotations_folder)
for ann in ann_list:
    ann_path = f"{pascal_annotations_folder}/{ann}"
    PascalVOC_to_YOLO(ann_path, output_folder)    