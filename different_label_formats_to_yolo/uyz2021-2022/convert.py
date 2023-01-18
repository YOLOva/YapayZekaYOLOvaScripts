

import xml.etree.ElementTree as ET
from pathlib import Path
import os

class YoloAnnotation():
  def __init__(self, txt_path ) -> None:
    self.txt_path = txt_path
    self.text = ""
  def addObject(self, cls, x_ctr, y_ctr, width, height):
    object_line = f'{cls} {x_ctr} {y_ctr} {width} {height}/n'
    self.text = f"{self.text}{object_line}"
      
  def write_output(self):
    with open(self.txt_path, 'w') as f:
      f.write(f'{self.text}')
      f.close()

name_to_id = {
    "Taşıt":0,
    "İnsan":1,
    "UAP":2,
    "UAİ":4
}

def PascalVOC_to_YOLO_UYZ(input_path, output_folder):
  tree = ET.parse(input_path)#Xml ayrıştırılır
  root = tree.getroot()#root köke ulaşılır
  txt_filename = input_path.name
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
    x_ctr = (xmin + (o_width/2))
    y_ctr = (ymin + (o_height/2))
    id = name_to_id[name]
    if name in ["UAP", "UAİ"]:
      fattributes = fobject.find("attributes")
      for attribute in fattributes.findall("attribute"):
        if attribute.find("name").text == "İnilebilir" and attribute.find("value").text!="True":
          #print(input_path)
          id+=1
          break
    yolo_annotation.addObject(id, x_ctr, y_ctr, o_width, o_height)
  yolo_annotation.write_output()



from_path = "D:/Teknofest/YOLOVA/Veriseti/New/2022Oturumlar/oturum2_nt/"
to_path = "D:/Teknofest/YOLOVA/Veriseti/New/2022Oturumlar/oturum2_new/"


anns = list(Path(from_path).glob("**/*.xml"))
print(len(anns))
for ann in anns:
    xml_dir=str(ann).replace("\\","/", -1)
    txt_path = xml_dir.replace("oturum2_nt", "oturum2_new").replace(".xml", ".txt").replace("Annotations/Annotations/","labels/")
    filename = Path(txt_path).name
    txt_folder = txt_path.replace(filename, "")
    Path(txt_folder).mkdir(parents = True, exist_ok = True)
    if "VY2_2" in txt_folder:
        print(ann)
    PascalVOC_to_YOLO_UYZ(ann, txt_folder)

""" for folder_path in os.listdir(from_path):
  ann_folder =from_path+folder_path+"/Annotations/Annotations/"
  for xml_path in Path(ann_folder).glob("*.xml"):
    xml_dir = str(xml_path).replace("\\","/", -1)
    txt_path = xml_dir.replace("oturum2_nt", "oturum2_new").replace(".xml", ".txt").replace("Annotations/Annotations/","labels/")
    filename = Path(txt_path).name
    txt_folder = txt_path.replace(filename, "")
    Path(txt_folder).mkdir(parents = True, exist_ok = True)
    PascalVOC_to_YOLO_UYZ(xml_path, txt_folder) """