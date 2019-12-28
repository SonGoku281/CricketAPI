# since the cricksheet is downloaded in yaml format we need to parse each file and get the data into our database
import os
import yaml

path = "./allMatches"
count = 0 
for filename in os.listdir(path):
    if filename.endswith(".yaml"): 
         # parse the yaml file and fill the database.
         with open(path+"/"+filename) as f:
            # use safe_load instead load
            dataMap = yaml.safe_load(f) 
            count = count + 1
    f.close()
    
count = count +1