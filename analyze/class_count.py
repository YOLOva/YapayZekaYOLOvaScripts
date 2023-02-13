from pathlib import Path


classes_txt = r"classes.txt"

with open(classes_txt, "r") as f:
    class_list = [x.replace("\n", "") for x in f.readlines()]


dataset_folder_path = r"D:\Teknofest\YOLOVA\Veriseti\KesisenYol"


class_count_list = {id: {"name": name, "count": 0}
                    for id, name in enumerate(class_list)}

for txt_path in Path(dataset_folder_path).glob("**/*.txt"):
    txt_path = str(txt_path)
    if "classes.txt" in txt_path:
        continue

    with open(txt_path) as f:
        lines = f.readlines()
        for line in lines:
            cols = line.split()
            cls = int(cols[0])
            class_count_list[cls]["count"] += 1

for key, data in class_count_list.items():
    print(f"{data['name']}: {data['count']}")
