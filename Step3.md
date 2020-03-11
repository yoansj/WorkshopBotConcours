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

Great you found words that indicates that you must follow the users but how to follow the users :question:

Firstly you will declare a member variable in your class called usernames it will be a list so initialize it by doing so :

```python3
usernames = list()
````
We want the bot to do the following thing :
* Searching for words that indicates if we must follow the users
* If we found a word start the search for usernames
    * Search every @ in the tweet text
    * For each @ character after the @ check if the char is a char that can be in a username
    * If so add the char in a temporary variable
    * If the char is not a user char break and check for the next @ in the tweet

To do so use the following functions :

```python3
    # Fonction qui permet de checker si le caractère est un caractère du username
    def isLetter(self, letter):
        letters = "azertyuiopqsdfghjklmwxcvbn0123456789_" # Ce sont tous les caractères qui peuvent être présents dans un nom d'utilisateur twitter
        for l in letters:
            if letter == l:
                return True
        return False

    #Fonction qui récupére tous les utilisateurs
    #Complétez la fonction suivante en remplaçant les XXX
    def findUser(self, index, tweet_text):
        find = tweet_text.find(XXX, index)
        tempUserName = ""
        if find != -1:
            find += 1
            for letter in tweet_text[find: :1]:
                # Il faut checker à la ligne du dessous si la lettre fait parti des caractères autorisés dans un pseudo
                # La fonction est censée marcher avec les majuscules et les minuscules (utilisez .lower)
                if XXX == True:
                    tempUserName = tempUserName + letter
                else:
                    break
            self.XXX # A cette ligne il faut ajouter le pseudo dans la liste des utilisateurs qu'on va follow
            if tweet_text.find(XXX, find + 1) != -1:
                self.findUser(find + 1, tweet_text)
    
    #Fonction qui permet de follow tous les utilisateurs
    #Complétez la fonction suivante en remplaçant les XXX  
    def followUsers(self):
        for user in self.###:
            try:
                XXX # Ligne ou on follow l'utilisateur
            except:
                print("Error while following user :", user) # Si on arrive pas à follow l'utilisateur
```

Once you completed this, your bot should be able to like, retweet and follow the users to enter contests :happy:

### Wait it's not over

If you succeded the 3 steps you have a basic bot that enters contests but you can improve the bot on many aspects :thinking:

Here is a list of functionnalities that you can make that will improve your bot, you can do them in any order

* Check if the tweet is a contest by searching for words that indicate it (**you should start by this one**)
* Create a log system that writes in a file the actions that your bot are doing
* Simmilary to the like and rt functionnality create a tag functionnality that identifies other accounts when it's needed
* Create a configuration file that lets you changes the words or other settings of the bot easily
* Create a system that automatically relaunch your bot when it crashes or when it stopps
