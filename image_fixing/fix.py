
from PIL import Image
from pathlib import Path

images = list(Path("D:/Teknofest/YOLOVA/Veriseti/New/2022Oturumlar/oturum2/oturum2_Azaltildi/images").glob("**/*.jpg"))
for image_path in images:
  im1 = Image.open(image_path)
  new_image = Path(str(image_path).replace("\images", "\images_new"))
  print(new_image)
  im1.save(new_image)