import json
import twitter
import oauth_login

def twitter_trends(twitter_api,woe_id):
    return twitter_api.trends.place(_id=woe_id)


twitter_api=oauth_login.oauth_login()
#WORLD_WOE_ID =1
#world_trends=twitter_trends(twitter_api,WORLD_WOE_ID)
#print json.dumps(world_trends,indent=1)

INDIA_WOE_ID=23424848
trends=twitter_trends(twitter_api,INDIA_WOE_ID)
print json.dumps(trends,indent=1)

#USA_WOE_ID=23424977
#trends=twitter_trends(twitter_api,USA_WOE_ID)
#print json.dumps(trends,indent=1)

#RUSSIA_WOE_ID=23424936
#trends=twitter_trends(twitter_api,RUSSIA_WOE_ID)
#print json.dumps(trends,indent=1)
