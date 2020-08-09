#!/usr/bin/env python3
import os
import emails
import glob
import reports
import datetime
today=datetime.date.today()
files = glob.glob("supplier-data/descriptions/*.txt")
def generate_pdf():
  paragraph = ""
  for file in files:
    with open(file) as f:
      paragraph += "name: " + f.readline().rstrip() + "<br/>"
      paragraph += "weight: " + f.readline().rstrip() + "<br/><br/>"
  new_file="/tmp/processed.pdf"
  title= "Processed Update on "+today.strftime("%A") + " " + today.strftime("%d") + ", " + today.strftime("%Y")
  if reports.generate_report(new_file,title,paragraph):
    return "PDF Generate"
  else:
    return "Something Went Wrong"

#SEND EMAIL
if __name__ == "__main__":
  print(generate_pdf())

  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  new_file="/tmp/processed.pdf"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  attachment = new_file
  new_email = emails.generate_email(sender, receiver, subject, body, attachment)
  emails.send_email(new_email)
