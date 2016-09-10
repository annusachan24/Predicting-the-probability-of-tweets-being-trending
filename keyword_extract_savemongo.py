import json
import pymongo
import re
import oauth_login
import keyword_extract
import twitter
import savemongo

twitter_api=oauth_login.oauth_login()
q = 'Kumar Vishwas'
count=10
search_results = keyword_extract.twitter_search(twitter_api,q,count)
print json.dumps(search_results,indent=1)

savemongo.save_to_mongo(search_results,'tweets','8/08Kumar Vishwas')
#results= load_from_mongo('tweets','Scorpion')
#st=results[111]['text']
#print st
