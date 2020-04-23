import tweepy # Pour twitter
import time # Pour pouvoir sleep
import datetime # Pour la date
from datetime import datetime # Pour la date aussi

## Connection a Twitter
# Ajoutez les clés de votre application juste ici
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#Date minimale
TWEET_MIN_DATE = datetime(2020, 4, 7)

#Followers minimum à avoir
TWEET_FOLLOWERS_MIN = 1500

# Mots concours
TWEET_CONTEST_WORDS = ["gagner", "participer", "concours", "offrir", "donner", "nintendo switch"]
#Mots pour RT
TWEET_RT_WORDS = ["rt ", "partage", "retweeter", "retweete", "commenter", "commentez", " rt "]
#Mots pour follow
TWEET_FOLLOW_WORDS = ["follow", "suivre", "abonne", "abonne toi", "abonné"]
#Mots pour identifier
TWEET_TAG_WORDS = ["tag", "tagguez", "ami", "vrais ami", "potes", "khey", "friend", "bro"]
#Utilisateurs à identifier
TWEET_TAG_USERS = "@cyprien @elonmusk @tontongibs @realdonaldtrump @alderiate"

class MonBot(tweepy.StreamListener):

    def getTweetUrl(self, tweet, tweet_text):
        # Cherche l'URL d'un tweet dans un texte
        return

    def searchWord(self, tweet, tweet_text, words):
        # Cherche dans un texte un des mots contenus dans un tableau de texte
        text = tweet_text.lower()
        to_return = ""
        for word in words:
            if word in text:
                to_return += word + ";"
        if to_return == "":
            return False
        return to_return

    def isLetter(self, letter):
        # Permet de vérifier si le caractère passé en param est bien autorisé dans un @ twitter
        # return True ou False
        letters = "azertyuiopqsdfghjklmwxcvbn0123456789_"
        for l in letters:
            if letter == l:
                return True
        return False

    def findUser(self, index, tweet_text):
        find = tweet_text.find("@", index) # On cherche le @ a partir de index
        tempUserName = ""
        if find != -1:
            find += 1
            # Itérer à travers le texte
            for letter in tweet_text[find: :1]:
                if self.isLetter(letter.lower()) == True:
                    tempUserName = tempUserName + letter
                else:
                    break
            self.usernames.append(tempUserName) # On ajoute le pseudo à la liste
            if tweet_text.find("@", find + 1) != -1: # Si on trouve un autre @ on relance la fonction
                self.findUser(find + 1, tweet_text)

    def findUsernames(self, tweet, tweet_text):
        self.usernames = []
        find_result = tweet_text.find("@") # Premier find pour savoir si il y a bien un @ dans le texte
        if find_result == -1:
            print("On follow l'auteur du tweet : " + tweet.user.screen_name)
            self.usernames.append(tweet.user.screen_name)
            return
        else:
            self.findUser(find_result, tweet_text)

    def followUsers(self):
        for user in self.usernames:
            try:
                api.create_friendship(user)
                api.create_mute(user)
            except:
                print("Error on pas pu follow :", user)
        self.usernames = []

    def on_status(self, status):

        print("--- Nouveau tweet ---")

        # Cette partie du code permet de savoir si le tweet est un Retweet
        # http://docs.tweepy.org/en/latest/extended_tweets.html#examples

        if hasattr(status, 'retweeted_status'):
            try:
                tweet_text = status.retweeted_status.extended_tweet["full_text"]
                self.isRetweet = True
            except:
                tweet_text = status.retweeted_status.text
                self.isRetweet = False
        else:
            try:
                tweet_text = status.extended_tweet["full_text"]
                self.isRetweet = False
            except AttributeError:
                tweet_text = status.text
                self.isRetweet = False

        # On affiche l'URL du tweet
        #print("URL : " + self.getTweetUrl(status, tweet_text))

        # On vérifie la date du tweet
        # Si la date est mauvaise on return
        if self.isRetweet == True:
            if status.retweeted_status.created_at < TWEET_MIN_DATE:
                print("Mauvaise date !")
                return
        else:
            if status.created_at < TWEET_MIN_DATE:
                print("Mauvaise date !")
                return

        #On regarde si on a déja like le tweet
        try:
            if self.isRetweet == False:
                api.create_favorite(status.id)
            else:
                api.create_favorite(status.retweeted_status.id)
        except tweepy.error.TweepError as error:
            if error.api_code == 139:
                print("Tweet déja process")
                return

        ## Vérifie le nombre de followers
        if self.isRetweet == True:
            if status.retweeted_status.user.followers_count < TWEET_FOLLOWERS_MIN:
                print("Pas assez de followers")
                print("Auteur : " + str(status.retweeted_status.user.followers_count) + " Requis : " + str(TWEET_FOLLOWERS_MIN))
                return
        elif status.user.followers_count < TWEET_FOLLOWERS_MIN:
            print("Pas assez de followers")
            print("Auteur : " + str(status.user.followers_count) + " Requis : " + str(TWEET_FOLLOWERS_MIN))
            return


        # On regarde si le tweet est un concours
        # Si la fonction a return false alors on quitte
        words = self.searchWord(status, tweet_text, TWEET_TAG_WORDS)
        if words == False:
            print("Personne a tag")
        else:
            print("Mots trouvés tag : " + words)
            if self.isRetweet == True:
                api.update_status("@" + status.retweeted_status.user.screen_name + "\n" + TWEET_TAG_USERS, status.retweeted_status.id)
            else:
                api.update_status("@" + status.user.screen_name + "\n" + TWEET_TAG_USERS, status.id)

        # On regarde si on doit RT le tweet
        # Si la fonction a return false alors on fait rien
        words = self.searchWord(status, tweet_text, TWEET_RT_WORDS)
        if words == False:
            print("Personne RT")
        else:
            print("Mots trouvés RT : " + words)
            if self.isRetweet == False:
                api.retweet(status.retweeted_status.id)
            else:
                api.retweet(status.id)

        # On regarde si on doit follow des personnes
        # Si la fonction a return false alors on fait rien


        # On regarde si on doit identifier d'autres personnes
        # Si la fonction a return false alors on fait rien
        words = self.searchWord(status, tweet_text, TWEET_CONTEST_WORDS)
        if words == False:
            print("Pas un concours !")
            return
        print("Mots trouvés concours : " + words)


        # On sleep pour pas bypass les limites de requêtes
        print("Le bot se repose pendant 30s")
        time.sleep(60)


#On instancie un objet bot
#On le relie à notre objet api
bot = MonBot()
bot = tweepy.Stream(auth = api.auth, listener=bot)

#On lance le bot qui va chercher les termes suivants
bot.filter(track=["#concours", "#giveaway", "#cadeau", "#gift"])