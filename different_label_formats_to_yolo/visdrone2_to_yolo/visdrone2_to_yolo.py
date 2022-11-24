import os
from pathlib import Path

def visdrone2yolo(dir):
      from PIL import Image
      from tqdm import tqdm
      def convert_box(size, box):
          # Convert VisDrone box to YOLO xywh box
          dw = 1. / size[0]
          dh = 1. / size[1]
          return (box[0] + box[2] / 2) * dw, (box[1] + box[3] / 2) * dh, box[2] * dw, box[3] * dh

      Path(f"{dir}/labels").mkdir(parents=True, exist_ok=True)  # make labels directory
      pbar = tqdm(Path(f"{dir}/annotations").glob('*.txt'), desc=f'Converting {dir}')
      for f in pbar:
          img_size = Image.open(Path(f"{dir}/images/{f.name}").with_suffix('.jpg')).size
          lines = []
          with open(f, 'r') as file:  # read annotation.txt
              for row in [x.split(',') for x in file.read().strip().splitlines()]:
                  if row[4] == '0':  # VisDrone 'ignored regions' class 0
                      continue
                  cls = int(row[5]) - 1
                  box = convert_box(img_size, tuple(map(int, row[:4])))
                  lines.append(f"{cls} {' '.join(f'{x:.6f}' for x in box)}\n")
                  with open(str(f).replace(os.sep + 'annotations' + os.sep, os.sep + 'labels' + os.sep), 'w') as fl:
                      fl.writelines(lines)  # write label.txt

if __name__ == "__main__":
    target_dir = "D:/Teknofest/YOLOVA/Veriseti/Visdrone2019/VisDrone2019-DET-test-dev"
    visdrone2yolo(target_dir)