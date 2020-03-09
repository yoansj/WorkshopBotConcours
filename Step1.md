# Step 1 : Rt si t triste

## :question: Great links with answers to your questions
What is it ? | The link
-------------|---------
**Twitter developper**|https://developer.twitter.com/en.html
**Tweepy API**|http://docs.tweepy.org/en/latest/api.html
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
bot.filter(track=['#concours'])
```
## Exercise time

### Ex 01 : RT a simple tweet

The goal of this exercise will be to retweet a simple tweet linked [here](https://twitter.com/AlderiateTV/status/1229424056451182594)

This exercise isn't really complicated you just have to read the [documentation](http://docs.tweepy.org/en/latest/api.html)

**Pro tip** you can get a specific tweet by using the function ```api.get_status()```

### Ex 02 : RT a tweet with some conditions

Now that you know how to RT a tweet how about RT with some conditions ?

Create a function called doWeRT wich searches words into the tweet that indicate if we must retweet the tweet to join the contest.

```python
    def doWeRT(self, tweet, tweet_text):
        text = tweet_text.lower()
        to_return = ""
        words = ["#workshop", "#de", "#yoan"] #à changer par vos mots à vous :) :smile:
        for word in words:
            if word in text:
                to_return += word + ";"
        if to_return == "":
            return False
        return to_return
```
As you see this function returns False when it founds no words indicating that we must rt the tweet.

When it returns a non False value you must RT the tweet. The non False value corresponds to the words found you can print them to check what you got.

### Are you done ?

Does your bot RT the tweets only when it finds the words written in the doWeRT function ?

If yes head on to the next exercise :smile:
