import json
from pathlib import Path


json_path = "D:/Teknofest/YOLOVA/Veriseti/auair/annotations.json"
save_path = "D:/Teknofest/YOLOVA/Veriseti/auair/labels"

with open(json_path, "r") as file:
    data = json.load(file)

for annotation in data["annotations"]:
    image_name = annotation["image_name"]
    image_width = annotation["image_width:"]
    image_height = annotation["image_height"]
    bboxes = annotation["bbox"]
    lines = []
    for bbox in bboxes:
        top = bbox["top"]
        left = bbox["left"]
        height = bbox["height"]
        width = bbox["width"]
        cls = bbox["class"]

        cx = (left+width/2)/image_width
        cy = (top+height/2)/image_height
        w=width/image_width
        h=height/image_height

        lines.append(f"{cls} {cx} {cy} {w} {h}\n")
    Path(save_path).mkdir(parents=True, exist_ok=True)
    with open(f"{save_path}/{Path(image_name).stem}.txt", "w") as label_file:
        label_file.writelines(lines)


