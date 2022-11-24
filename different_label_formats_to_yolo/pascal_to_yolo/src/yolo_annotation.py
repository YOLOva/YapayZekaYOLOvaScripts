from pathlib import Path

class YoloAnnotation():
  def __init__(self, txt_path ) -> None:
    self.txt_path = txt_path
    self.text = ""
  def addObject(self, cls, x_ctr, y_ctr, width, height):
    object_line = f'{cls} {x_ctr} {y_ctr} {width} {height}\n'
    self.text = f"{self.text}{object_line}"
      
  def write_output(self):
    with open(self.txt_path, 'w') as f:
      f.write(f'{self.text}')
      f.close()