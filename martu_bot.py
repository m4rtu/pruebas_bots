import os
import sys
import copy
import time
import pickle
import random
from threading import Thread, Lock
from multiprocessing import Queue

try:
	import twitter
	IMPTWITTER = True
	print(u"libreria de twitter importada")
except:
	print(u"no se pudo importar la libreria de twitter.")
	IMPTWITTER = False

class MartuBot():

	def __init__(self):

		self._t = None
		self._ts = None

	#def read(self, filename)

	#	if not self._check_file(filename):
	#		self._error(u'read', u"no existe el archivo: '%s'" %(filename))
	#	
	#	with open(filename, u'r') as f:
	#	contents_line = f.readline()

	def twitter_login(self, cons_key, cons_secret, access_token, access_token_secret):
		self._oauth = twitter.OAuth(access_token, access_token_secret, cons_key, cons_secret)
		self._t = twitter.Twitter(auth=self._oauth)
		self._ts = twitter.TwitterStream(auth=self._oauth)
		self._loggedin = True
		self._credentials = self._t.account.verify_credentials()
		print(u"login!")

	def _twitear(self, tweet):
	
		tweet = self._t.statuses.update(status=tweet)





