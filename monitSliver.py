from fileinput import filename
import logging
import subprocess
import time
from urllib import request
import telegram_send

filename = '/root/.sliver/logs/audit.json'
timeout_time = 0;

f = subprocess.Popen(['tail','-F',filename],\
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)

while True:
    line = str(f.stdout.readline())
    result = line.split("\\")
    try:
      #pcname = result[26]
      report = "PC NAME: "+result[26].replace('"','')+"\nUSERNAME "+result[50].replace('"','')+"\nIMPLANT: "+result[18].replace('"','')+"\nIPADD:PORT "+result[98].replace('"','')
      #print(report)
      telegram_send.send(messages=[report])
    except:
      None
