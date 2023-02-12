
from pathlib import Path
import xml.etree.ElementTree as ET
from os.path import join
from pathlib import Path
import cv2
name_to_id = {
    "car":5,
    "person": 0
}
def convert_semantic_annotation_to_Yolov5(xml_file, image_folder, output):
    image_file = join(image_folder,f"{Path(xml_file).stem}.jpg")
    with open(xml_file, "rb") as xml_file_value:
        try:
            #print(image_file)
            objects = ET.fromstring(xml_file_value.read()).findall("object")
            iheight, iwidth, _ = cv2.imread(image_file).shape
            Path(output).mkdir(parents = True, exist_ok = True)
            with open(join(output, f"{Path(xml_file).stem}.txt"), "w") as f:
                for fobject in objects:
                    object_name = fobject.find("name").text
                    xmax, ymax, xmin,ymin = 0,0,0,0
                    if object_name in name_to_id.keys():
                        pts = fobject.find("polygon").findall("pt")
                        xs = []
                        ys = []
                        for pt in pts:
                            xs.append(float(pt.find("x").text))
                            ys.append(float(pt.find("y").text))
                        xmin = min(xs)/iwidth
                        ymin = min(ys)/iheight
                        xmax = max(xs)/iwidth
                        ymax = max(ys)/iheight
                        width = xmax- xmin
                        height = ymax-ymin
                        cx = (xmax+xmin)/2
                        cy = (ymax+ymin)/2
                        class_id = name_to_id[object_name]
                        f.write(f'{class_id} {cx} {cy} {width} {height}\n')
        except:
            print(f"hata: {xml_file}")

from os.path import join
import os
folder = r"D:\Teknofest\YOLOVA\Veriseti\SemanticDrone\training_set\gt\semantic\label_me_xml"
for file in Path(folder).glob("*.xml"):
  convert_semantic_annotation_to_Yolov5(file, r"D:\Teknofest\YOLOVA\Veriseti\SemanticDrone\training_set\images", r"D:\Teknofest\YOLOVA\Veriseti\SemanticDrone\training_set\labels")