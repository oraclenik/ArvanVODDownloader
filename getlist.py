import json
from extract import json_extract
from requests.exceptions import HTTPError
import urllib.request

def getjson(URL, header):
    try:
        req = urllib.request.Request(url=URL, headers=header)
        res = urllib.request.urlopen(req, timeout=5)
        res_body = res.read()
        j = json.loads(res_body.decode("utf-8"))
        return j
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')    

def getchannellist(APIURL, APIKEY, PERPAGE):
    URL = str(str(APIURL)+"/channels?per_page="+PERPAGE)
    headers = {'Authorization': APIKEY,}
    channellist = getjson(URL, headers)
    return channellist

def getmp4urls(APIURL, APIKEY, CHANNELIDS):
    headers = {'Authorization': APIKEY,}
    mp4urls=list()

    for id in CHANNELIDS:
        URL = str(APIURL)+"/channels/"+str(id)+"/videos"+"?per_page=9999"
        j = getjson(URL, headers)
        if j:
            for prefix in j['data']:
                mp4_urls=(prefix['mp4_videos'])
                #mp4_title=(prefix['title'])
                fileinfo=[mp4_urls]
                mp4urls.append(fileinfo)
    return mp4urls