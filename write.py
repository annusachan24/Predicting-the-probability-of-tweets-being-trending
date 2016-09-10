import savemongo
import json
import re

results=savemongo.load_from_mongo('tweets','4/08Scorpion')
f=open("data.txt","w")
for i in range(len(results)):
    print results[i]['text']
    f.write(results[i]['text'].encode("utf-8"))
f.close()
    
