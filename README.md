# py-Image-segmentation

Project for developing an "intelligent" object segmentation from an image using interactive tools. The inteded goal is for the user to select an object from an image using one click and the object is selected automatically. Right now the object selection is based on a specified guess of object size. 

# bbox-selector.py

bboxox-selector.py in the scripts directory goes through images in a given directory and displays the images one-by-one. For each image displayed, the user selects two points that correspond to the upper-right and lower-left coordinates of a bounding box. bbox-selector.py then takes these provided bounding box coordinates and crops the images and saves to a specified target directory. The cropped image that is saved in the target directory will have the same filename as the displayed image but prepended with the string "cropped_"

Currently the directory images to crop and directory of cropped images to save are specified by the src_path and out_path variables respectively:

```
src_path = "../images/dir1/"
out_path = "../images/cropped/"
```


# Installation

Easiest way is to download this entire repository. The pylab and PIL libraries are required. Tested on python 2.7

# Tests

If the entire repository has been download, then in terminal or command prompt go to the scripts directory and run 
```
python bbox-selector.py
```

This will show the images in the images/dir1/ directory. Once the user selects the bounding boxes for all images, the cropped images can be found in images/cropped/

