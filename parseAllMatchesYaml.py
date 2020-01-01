# since the cricksheet is downloaded in yaml format we need to parse each file and get the data into our database
import os
import yaml
import setupDB
import multiprocessing
import concurrent.futures
def parseMatches(curr):
    path = "./allMatches"
    onlyfiles = len(next(os.walk(path))[2])
    for filename in os.listdir(path):
        parseEachFile(path,filename,curr)

def parseEachFile(path,filename,curr):
     if filename.endswith(".yaml"): 
             # parse the yaml file and fill the database.
            with open(path+"/"+filename) as f:
                # use safe_load instead load
                dataMap = yaml.safe_load(f) 
                # update the tables using the datamap
                setupDB.updateTables(curr,dataMap,filename)
            f.close()
