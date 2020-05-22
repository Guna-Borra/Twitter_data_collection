import tweepy
import sys
import json
import yweather

# authorization tokens
consumer_key = "KTVTkpZvAMz0wifJxj3gJXI1v"
consumer_secret = "i1w9FA6GlyBhSQijH3IJlahGcdQXTLhqcq4rsjoNXCRK8oPwXa"
access_key = "845647315167731713-SjRcGKIJmE4rSCtISBWUJx6Ni7JAdDA"
access_secret = "B9cbknyXz1Ts5oZu1AmlTEWO4L3w7WoxjeXYAS4dKDOSn"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

client = yweather.Client()
client.fetch_woeid('India')



# Where On Earth ID for Brazil is 23424768.
INDIA_WOE_ID = 2295414            
 #hyderbad  :2295414
 # india : 2282863
india_trends = api.trends_place(INDIA_WOE_ID)
 
trends = json.loads(json.dumps(india_trends, indent=1))
 
for trend in trends[0]["trends"]:
	print (trend["name"])