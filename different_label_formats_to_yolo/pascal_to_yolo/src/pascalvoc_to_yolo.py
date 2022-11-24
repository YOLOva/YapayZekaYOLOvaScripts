import xml.etree.ElementTree as ET
from pathlib import Path
from src.yolo_annotation import YoloAnnotation

def PascalVOC_to_YOLO(input_path, output_folder):
  Path(output_folder).mkdir(exist_ok=True)
  tree = ET.parse(input_path)#Xml ayrıştırılır
  root = tree.getroot()#root köke ulaşılır
  txt_filename = f"{Path(input_path).stem}.txt"
  size = root.find("size")
  width = int(size.find("width").text)
  height = int(size.find("height").text)
  yolo_annotation = YoloAnnotation(f"{output_folder}/{txt_filename}") 
  objects = root.findall('object')#root elemanın, object türündeki elemanlarını alıyoruz
  for fobject in objects:
    name = str(fobject.find('name').text)
    bbox = fobject.find('bndbox')
    xmin = float(bbox.find('xmin').text)/width
    ymin = float(bbox.find('ymin').text)/height
    xmax = float(bbox.find('xmax').text)/width
    ymax = float(bbox.find('ymax').text)/height
    o_width = xmax-xmin
    o_height = ymax-ymin
    x_ctr = (xmin + xmax)/2
    y_ctr = (ymin + ymax)/2
    yolo_annotation.addObject(name, x_ctr, y_ctr, o_width, o_height)
  yolo_annotation.write_output()