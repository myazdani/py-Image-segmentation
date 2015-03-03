from PIL import Image
from pylab import *

in_file = "../images/Lenna.png"
out_file = "../found_items/image_segment.jpg"

segment_dim = 10

im = array(Image.open(in_file))
imshow(im)
x = ginput(1)
cla()
print 'you clicked:', x
show()

image_segments = im[x[0][0]-segment_dim:x[0][0]+segment_dim, x[0][1]-segment_dim:x[0][1]+segment_dim, :]

Image.fromarray(uint8(image_segments)).save(out_file)

