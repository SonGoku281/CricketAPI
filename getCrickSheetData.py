import urllib3
import zipfile
import os
from bs4 import BeautifulSoup

def getDatafromCrickSheet():
    ziplink = 'https://cricsheet.org/downloads/all.zip'
    https = urllib3.PoolManager()
    response = https.request("GET",ziplink)

    filename = 'cricksheet.zip'
    path = os.getcwd()
    f = open(filename, 'wb')
    f.write(response.data)
    f.close()
    response.release_conn()
    with zipfile.ZipFile(path+"/"+filename, 'r') as zip_ref:
        zip_ref.extractall(path+"/allMatches")

