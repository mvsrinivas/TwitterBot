import tweepy
import time
import test

client = tweepy.Client(
       consumer_key=test.api_key,
       consumer_secret=test.api_key_secret,
       access_token=test.access_token,
       access_token_secret=test.access_token_secret
)
 
class retweetTweetListener(tweepy.StreamingClient):
        
    def on_tweet(self, tweet):
        if tweet.referenced_tweets == None:
            client.retweet(tweet.id)
            print("retweeted successfully")
            time.sleep(2)

def main():
    
    auth = tweepy.OAuth1UserHandler(test.api_key,test.api_key_secret, test.access_token, test.access_token_secret)
    api = tweepy.API(auth)
    time.sleep(0.3)
    tweets_listener = retweetTweetListener(test.bearer_token)
    tweets_listener.add_rules(tweepy.StreamRule("(#techhiring) (-is:retweet)"))
    tweets_listener.filter(tweet_fields = ["referenced_tweets"])

if __name__ == "__main__":
    main()



