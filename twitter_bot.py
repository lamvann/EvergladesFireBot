import tweepy as tp


# credentials to login to twitter api
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

# Get previous tweets
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

# Tweet 3 times in a row as test
api.update_status('hello from automated python 🙂 tweet #' + str(1) + " of the day.")
