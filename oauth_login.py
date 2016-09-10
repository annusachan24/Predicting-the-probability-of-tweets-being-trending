import twitter

def oauth_login():
    CONSUMER_KEY='lLbM3j62fylgYa6As6PqQLJEs'
    CONSUMER_SECRET='CAMdOrUOoPC5mFHON4QFOCh6c6hLGLmTdKlUfGFxRFtJLSC6PV'
    OAUTH_TOKEN='2578113254-babJP0rX9n3lGOpLWJfB2rkzJIdPzsxnAB6Xsea'
    OAUTH_TOKEN_SECRET='UgVoO3fLNyPbqEnmvqjXFb8A1kx3l3KxpUwIhAYP2OkJp'

    auth=twitter.oauth.OAuth(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET)
    
    twitter_api=twitter.Twitter(auth=auth)

    return twitter_api

twitter_api=oauth_login()

print twitter_api
