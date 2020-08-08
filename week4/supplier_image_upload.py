#!/usr/bin/env python3

import requests
import glob

url="http://localhost/upload/"

files = glob.glob("supplier-data/images/*.jpeg")

for file in files:
	with open(file,'rb') as opened:
		r=requests.post(url,files={'file':opened})

