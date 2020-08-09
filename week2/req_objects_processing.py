
#!/usr/bin/env python3

import os
import requests


files = os.listdir("/data/feedback")
url = "http://35.239.197.142/feedback/"

for file in files:
        dict = {}
        lines = []
        with open("/data/feedback/"+file) as f:
                for line in f:
                        lines.append(line[:-1])

                dict["title"] = lines[0]
                dict["name"]= lines[1]
                dict["date"]=lines[2]
                dict["feedback"]=lines[3]
                print(dict["title"])
                req = requests.post(url,data=dict)
                print(req.raise_for_status())
