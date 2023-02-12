from pathlib import Path


classes_txt=r"classes.txt"

with open(classes_txt, "r") as f:
    class_list= [x.replace("\n", "") for x in f.readlines()]


dataset_folder_path= r"D:\Teknofest\YOLOVA\Veriseti\KesisenYol"


class_count_list=[0]*len(class_list)

for txt_path in list(Path(dataset_folder_path).glob("**/*.txt")):
    txt_path=str(txt_path)
    if "classes.txt" in txt_path:
        continue

    with open(txt_path) as f:
        lines=f.readlines()
        for line in lines:
            cols=line.split()
            cls=int(cols[0])
            class_count_list[cls]+=1

for i, count in  enumerate(class_count_list):
    print(f"{count} sayıda {class_list[i]}")