import os
import sys
from martu_bot import MartuBot

#crear el objeto bot de tipo MartuBot
bot = MartuBot()

#parsear claves desde un archivo

#file = open("claves.txt", "r")

#linea = file.readlines()
#cons_key = linea[0]
#cons_secret = linea[1]
#access_token = linea[2]
#access_token_secret = linea[3]


# ALL YOUR SECRET STUFF!
# Consumer Key (API Key)
cons_key = 
# Consumer Secret (API Secret)
cons_secret = 
# Access Token
access_token = 
# Access Token Secret
access_token_secret = 


# Log in to Twitter
bot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)


#twitear algo
tweet = sys.argv[1]
bot._twitear(tweet)


