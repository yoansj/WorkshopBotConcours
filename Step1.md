# Step 1 : Rt si t triste

## :question: Great links with answers to your questions
What is it ? | The link
-------------|---------
**Twitter developper**|https://developer.twitter.com/en.html
**Tweepy API**|https://www.tweepy.org
---

## Basics of the API
In this part of the workshop you will learn basic notions about the Twitter API.

In the previous example you saw how to get tweets in your code with a call to the API with the function ```api.home_timeline()```

Each call to the API is stored by Twitter and you have a minimum amount of call to the API every day.
Each call to the API is precious so be carefull when you make a call to the API. You can see all the limits on [this page](https://developer.twitter.com/en/docs/basics/rate-limits).

Now that you know how to get the tweets in your timeline you would like to have a bot that runs **infinitely** right ?
In C you would use a ```while``` loop, well in python this is a bit trashy :poop: and Tweepy already gives you the tools to do that.

**The streams** 

A stream let's you track tweets with specific keywords or tweets made by a specific user.
Paste the following code in a .py file and try to understand it :
Feel free to modify this code

```python
import tweepy

class MyAmazingBot(tweepy.StreamListener):

    #This function is called when a new tweet is received
    def on_status(self, status):
        if hasattr(status, "retweeted_status"):  # Check if Retweet
            try:
                print(status.retweeted_status.extended_tweet["full_text"])
        except AttributeError:
            print(status.retweeted_status.text)
        else:
            try:
                print(status.extended_tweet["full_text"])
            except AttributeError:
                print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False
        # returning non-False reconnects the stream, with backoff.


#This part of the code connects your Bot to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Creates your Stream
bot = MyAmazingBot()
bot = tweepy.Stream(auth = api.auth, listener=bot)

#Launches your bot
bot.filter(track=['#botconcours'])
```
## Exercise time

### Ex 01 : RT a simple tweet

The goal of this exercise will be to retweet a simple tweet linked [here](https://twitter.com/AlderiateTV/status/1229424056451182594)
This exercise isn't really complicated you just have to read the documentation
**Pro tip** you can get a specific tweet by using the function ```api.get_status()```
