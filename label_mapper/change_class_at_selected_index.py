from pathlib import Path


txt_dir=r"D:\Teknofest\YOLOVA\Veriseti\video\oversized_cargo\labels"
row=2
class_id=8

def change_value(path, column, row, new_value):
    lines = []
    with open(path, 'r+') as file:
        for line in file:
            lines.append(line.rstrip().split())
        print(lines)
        lines[row][column] = str(new_value)
        file.seek(0)
        for line in lines:
            line[-1] += "\n"    # or "\r\n" on windows
            file.write(' '.join(line))

for path in list(Path(txt_dir).glob("**/*.txt")):
    if "classes.txt" in str(path):
        continue
    change_value(path, 0, row, class_id)


