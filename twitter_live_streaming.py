import tweepy
import sys

# authorization tokens
consumer_key = "KTVTkpZvAMz0wifJxj3gJXI1v"
consumer_secret = "i1w9FA6GlyBhSQijH3IJlahGcdQXTLhqcq4rsjoNXCRK8oPwXa"
access_key = "845647315167731713-SjRcGKIJmE4rSCtISBWUJx6Ni7JAdDA"
access_secret = "B9cbknyXz1Ts5oZu1AmlTEWO4L3w7WoxjeXYAS4dKDOSn"


# StreamListener class inherits from tweepy.StreamListener and overrides on_status/on_error methods.
class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.id_str)
        # if "retweeted_status" attribute exists, flag this tweet as a retweet.
        is_retweet = hasattr(status, "retweeted_status")
        
         # check if text has been truncated
        if hasattr(status,"extended_tweet"):
            text = status.extended_tweet["full_text"]
        else:
            text = status.text
            
            
         # check if this is a quote tweet.
        is_quote = hasattr(status, "quoted_status")
        quoted_text = ""
        if is_quote:
            # check if quoted tweet's text has been truncated before recording it
            if hasattr(status.quoted_status,"extended_tweet"):
                quoted_text = status.quoted_status.extended_tweet["full_text"]
            else:
                quoted_text = status.quoted_status.text



         # remove characters that might cause problems with csv encoding
        remove_characters = [",","\n"]
        for c in remove_characters:
            text.replace(c," ")
            quoted_text.replace(c, " ")

        with open("out1.csv", "a", encoding='utf-8') as f:
            f.write("%s,%s,%s,%s,%s,%s\n" % (status.created_at,status.user.screen_name,is_retweet,is_quote,text,quoted_text))

    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")
        sys.exit()
        
        
if __name__ == "__main__":
    # complete authorization and initialize API endpoint
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize stream
    streamListener = StreamListener()https://codebeautify.org/jsonviewer/f83352
    stream = tweepy.Stream(auth=api.auth, listener=streamListener,tweet_mode='extended')
    with open("out1.csv", "w", encoding='utf-8') as f:
        f.write("date,user,is_retweet,is_quote,text,quoted_text\n")
    tags = ["RBI"]
    stream.filter(track=tags)