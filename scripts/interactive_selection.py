from PIL import Image
from pylab import *

in_file = "../images/Lenna.png"
out_file = "../found_items/image_segment"

segment_dim = 24
pil_im = Image.open(in_file)
im = array(pil_im)
imshow(im)
plot(0,0,'r*')
axis('off')
selections = ginput(3)
close()
print 'you clicked:', selections

imshow(im)
for i, selection in enumerate(selections):
	box = (int(selection[0])-segment_dim, int(selection[1])-segment_dim, int(selection[0])+segment_dim, int(selection[1])+segment_dim)
	plot([box[0], box[0]], [box[1], box[3]], 'b')
	plot([box[0], box[2]], [box[1], box[1]], 'b')
	axis('off')

	pil_im.crop(box).save(out_file + "_" + str(i) + ".jpg")

show()