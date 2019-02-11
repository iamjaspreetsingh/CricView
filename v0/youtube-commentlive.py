#!/usr/bin/python

# Usage:
# python sample.py --videoid='<video_id>'

import httplib2
import os
import sys
import json
from firebase import firebase

from apiclient.discovery import build_from_document
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow
import requests
firebase=firebase.FirebaseApplication("https://lifesaver-18f28.firebaseio.com/")
c=0
def callApi():
  auth_token='ya29.GlysBgCZyVdp_6YRh7AbUcUji8_ugz1dXE-zjeHlkllJA5-6JLw1h1DHEOeIl3n1IY90cAlyOr54eCj5-YPIvY4WCxjJaIskcTk_9LW0rY-UrqILgLnmdu-Ycj4f7g'
  hed = {'Authorization': 'Bearer ' + auth_token}
  response = requests.get("https://www.googleapis.com/youtube/v3/liveChat/messages?liveChatId=EiEKGFVDMExWM0xVSk9YYlozSEF3T3I2SG9sQRIFL2xpdmU&part=snippet",headers=hed)
  data=response.json()
  length=len(data['items'])
  comment=data['items'][length-1]['snippet']['displayMessage']
  return comment
while True:
  comment=callApi()
  print(comment)
  if "extreme left" == comment:
    res=firebase.put("/","dir",1)
  if "left" == comment:
    res=firebase.put("/","dir",2)  
  elif "right" == comment:
    res=firebase.put("/","dir",4)
  
  elif "extreme right" == comment:
    res=firebase.put("/","dir",5)

  elif "zoom" == comment:
      if c==0:
        c=1
        res=firebase.put("/","zoom",c)
      elif c==1:
        res=firebase.put("/","zoom",2)


# Call the API's commentThreads.list method to list the existing comment threads.






if __name__ == "__main__":
  callApi()