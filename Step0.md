# Step 0 : Prerequesites

# Python :snake:
For this workshop you need to have python3 installed on your system
To check if you have python open a new terminal use this command
```terminal
python3
```
If you don't have python3 install it with

### For Fedora
```terminal
sudo dnf install python37
```
### For Ubuntu (only for big brains)
```terminal
sudo apt-get install python3.7
```

# Tweepy :bird:
Next you need to install the Twitter API for python Tweepy

```terminal
pip3 install tweepy
```

# Create a Twitter developper account :bird:
This one will take time, be carefull and do **all the things that are said** :warning:

If you need help simply ask for it ! :question:

First things first go on the [Twitter developper](https://developer.twitter.com/en/apply-for-access) website and apply for access.

You will need a valid phone number and you will have to enter some text, the text doesn't really matters but you still have to enter it.

Once your developper account is created go to [your apps](https://developer.twitter.com/en/apps) and hit the **Create an app button**.
Fill all the required fields and create your app.

Once your app is created go to **Keys and tokens** and generate your **Consumer API keys** and your **Access token & access token secret**

If you successfully created your **developper account**, **your app** and **generated your keys** go on to the next step.
If not than do it, if you need help for this ask for it :smile:

# First contact :alien:
Create a new .py file and paste the following code in it

Change the values of ```consumer_key```, ```consumer_secret```, ```access_token``` and ```access_token_secret``` to the values of the keys that you generated on the previous step.

```python
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
```

Run the file with python3
```terminal
pyhton3 myfile.py
```

You should have a bunch of informations printed in your terminal
