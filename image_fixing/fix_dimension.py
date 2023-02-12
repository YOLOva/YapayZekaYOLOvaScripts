from pathlib import Path
import cv2
def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

images_path=r"D:\Teknofest\YOLOVA\Veriseti\video4\images"

for path in list(Path(images_path).glob("**/*.jpg")):
    path = str(path)
    frame = image_resize(cv2.imread(str(path)), width=1920)
    new_path=path.replace("\\", "/").replace("/images/", "/images_fixed/")
    Path(new_path).parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(new_path,frame)
    
    