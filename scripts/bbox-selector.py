import os
from PIL import Image
from pylab import *
 
src_path = "../images/dir1/"
out_path = "../images/cropped/"
image_type = ".jpg"
 
image_paths = []  
for root, dirs, files in os.walk(src_path):
  image_paths.extend([os.path.join(root, f) for f in files if f.endswith(image_type)])

for image_path in image_paths:
  pil_im = Image.open(image_path)
  im = array(pil_im)
  imshow(im)
  #plot(0,0,'r*')
  axis('off')
  selections = ginput(2)
  close()
  print 'you clicked:', selections

  box = (int(selections[0][0]), int(selections[0][1]), int(selections[1][0]), int(selections[1][1]))
  pil_im.crop(box).save(out_path + "cropped_" + image_path.split("/")[-1])