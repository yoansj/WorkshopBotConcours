# Step 3 : Vous SUIVEZ toujours ?

## :question: Great links with answers to your questions
What is it ? | The link
-------------|---------
**Twitter developper**|https://developer.twitter.com/en.html
**Tweepy API**|http://docs.tweepy.org/en/latest/api.html
---

## Exercise time

### Ex 01 : Following someone

The goal of this exercise is to learn how to follow someone, once again read the tweepy documentation :smile:

### Ex 02 : doWeFollow

The goal of this exercise is to make a simple function that searches for words indicating that we must follow the users

**Pro tip** read the Step02 pro tip.

### Ex 03 : Following everybody

Great you found words that indicates that you must follow the users, but now you must get all the users (@) in the tweet and follow them.

```python3
    def isLetter(self, letter):
        letters = "azertyuiopqsdfghjklmwxcvbn0123456789_" #Ce sont tous les caractères qui peuvent être présents dans un nom d'utilisateur twitter
        for l in letters:
            if letter == l:
                return True
        return False

    #Complétez la fonction suivante en remplaçant les croix XXX
    def findUser(self, index, tweet_text):
        find = tweet_text.find(XXX, index)
        tempUserName = ""
        if find != -1:
            find += 1
            for letter in tweet_text[find: :1]:
                if XXX == True: # Il faut checker à cette ligne si la lettre fait parti des caractères autorisés dans un pseudo, la fonction est censée marcher avec les majuscules et les minuscules (utilisez .lower)
                    tempUserName = tempUserName + letter
                else:
                    break
            self.usernames.append(tempUserName)
            if tweet_text.find(XXX, find + 1) != -1:
                self.findUser(find + 1, tweet_text)
```
