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
In C you would use a ```while``` loop, well in python this is a bit trashy and Tweepy already gives you the tools to do that.

**The streams** 
