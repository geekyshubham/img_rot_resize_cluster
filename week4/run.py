#! /usr/bin/env python3
import os
import glob
import requests
import json
files = glob.glob("supplier-data/descriptions/*.txt")
url ='http://35.232.67.151/fruits/'

def read_file():
  for file in files:
    dict={}
    lines=[]
    with open(file) as f:
      for line in f:
         lines.append(line[:-1])
      dict["name"]=lines[0]
      dict["weigth"]=int((lines[1])[:-3])
      dict["description"]=lines[2]
      dict["image_name"]=file[-7:-4]+".jpeg"
      print(dict)
      post_dict(dict)

def post_dict(dict_data):
  response = requests.post("http://35.232.67.151/fruits/", json=dict_data)
  if response.status_code == 201:
    print("Post to site successful for : ",dict_data["name"])
  else:
    print("Error while posting : " + dict_data['name'] + ", error code : " + str(response.status_code))

if __name__ == "__main__":
  read_file()


"""		
		req=requests.post(url,json=dict)
		print(req.raise_for_status())
"""
