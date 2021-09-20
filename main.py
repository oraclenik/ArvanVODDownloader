import getlist
from extract import json_extract
import csv 
import downloader
import os


print ("FYI : This Program only works on ubuntu or debian")

#Variables
APIURL= "https://napi.arvancloud.com/vod/2.0"
APIKEY= "Apikey <<PUTAPIKEYHERE>>"
DEBUG=True
Download=True
WriteToFile=True
DownloadOriginal=True
CSVFILE="URLFile.csv"
PERPAGE="9999"

#Debug
if DEBUG == True:
    print('Debug Mode is On')

#Flow
print ("-----------Getting Channels Lists-----------")
CHANNELLISTS= getlist.getchannellist(APIURL, APIKEY, PERPAGE)
if DEBUG == True:
    print (CHANNELLISTS)
    print (type(CHANNELLISTS))

print ("-----------Getting Channels IDS-----------")
CHANNELIDS= json_extract(CHANNELLISTS, 'id')
if DEBUG == True:
    print (CHANNELIDS)
    print (type(CHANNELIDS))

print ("-----------Getting MP4 URLS - Download and/or Write to file-----------")
mp4urls= getlist.getmp4urls(APIURL, APIKEY, CHANNELIDS, DownloadOriginal)
if WriteToFile == True:
    if os.path.exists(CSVFILE):
        os.remove(CSVFILE)
    for item in mp4urls:
        try:
            item
            f = open(CSVFILE, 'a')
            writer = csv.writer(f)
            writer.writerow(item)
            f.close()   
        except:
            print ("noitem")

if Download == True:
    for item in mp4urls:
        try:
            item
            downloader.downloader(item)
        except:
            print ("noitem")

