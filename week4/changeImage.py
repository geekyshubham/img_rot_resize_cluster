#!/usr/bin/env python3

from PIL import Image
import os
import glob

files =glob.glob("supplier-data/images/*.tiff")

for file in files:
	im = Image.open(file)
	resize = im.resize((600,400))
	out = resize.convert("RGB")
	out.save(file[:-4]+"jpeg","JPEG",quality=100)
