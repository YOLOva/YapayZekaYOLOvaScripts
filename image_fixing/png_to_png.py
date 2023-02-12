
from PIL import Image
from pathlib import Path

images = list(Path(r"D:\Teknofest\YOLOVA\Veriseti\uyz2021_o2\images").glob("**/*.png"))
for image_path in images:
  im1 = Image.open(image_path)
  new_image = Path(str(image_path).replace("\images", "\images_new").replace(".png", ".jpg"))
  new_image.parent.mkdir(parents=True, exist_ok=True)
  print(new_image)
  im1.save(new_image)