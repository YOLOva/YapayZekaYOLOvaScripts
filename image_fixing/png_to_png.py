
from PIL import Image
from pathlib import Path

images = list(Path(r"D:\Teknofest\YOLOVA\Veriseti\uyz2021\oturum6\images").glob("**/*.png"))
for image_path in images:
  im1 = Image.open(image_path)
  new_image = Path(str(image_path).replace("\images", "\images_new").replace(".png", ".jpg"))
  print(new_image)
  im1.save(new_image)