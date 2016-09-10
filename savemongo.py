import json
import pymongo
import re
import oauth_login
#import extract
import twitter

def save_to_mongo(data,mongo_db,mongo_db_coll,**mongo_conn_kw):
    client=pymongo.MongoClient(**mongo_conn_kw)
    db=client[mongo_db]
    coll=db[mongo_db_coll]
    return coll.insert(data)

def load_from_mongo(mongo_db,mongo_db_coll,return_cursor=False,criteria=None,projection=None,**mongo_conn_kw):
    client=pymongo.MongoClient(**mongo_conn_kw)
    db=client[mongo_db]
    coll=db[mongo_db_coll]

    if criteria is None:
        criteria={}

    if projection is None:
        cursor=coll.find(criteria)
    else:
        cursor=coll.find(criteria,projection)
    if return_cursor:
        return cursor
    else:
        return [item for item in cursor]

#twitter_api=oauth_login.oauth_login()

#INDIA_WOE_ID=23424977

#trends=extract.twitter_trends(twitter_api,INDIA_WOE_ID)

#print json.dumps(trends,indent=1)

#save_to_mongo(trends,'tweets','USA')
#results= load_from_mongo('tweets','USA')
