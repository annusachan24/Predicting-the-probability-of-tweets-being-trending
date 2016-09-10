import twitter
import json
import oauth_login


def twitter_search(twitter_api,q,max_results=400,*kw):
    search_results = twitter_api.search.tweets(q=q, count=100)
    statuses = search_results['statuses']
    max_results=min(1000,max_results)
    for _ in range(10):
        print "length of statuses", len(statuses)
        try:
            next_results=search_results['search_metadata']['next_results']
        except KeyError , e:
                break
        kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&")])
                         
        search_results = twitter_api.search.tweets(**kwargs)
        statuses += search_results['statuses']
        if len(statuses)>max_results:
            break
    return statuses                 
                     
                     
        
