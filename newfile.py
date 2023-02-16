from requests import get
from re import findall
import os
import glob
from libraryshad import robo_shad
import requests
from gtts import gTTS
from mutagen.mp3 import MP3
import json
from datetime import datetime
from json import loads , dumps
import time
from time import sleep
import random
import urllib.request
import io
from random import choice,randint
from PIL import Image
from colorama import Fore
from deep_translator import GoogleTranslator
from urllib import request

bot = robo_shad("")

target = bot.getInfoByUsername("amirreza51384")["user"]["user_guid"]

list_message_seened = []

while True:
	min_id = bot.getUserInfo(target)['chat']['last_message_id']
	try:
		
		while 1:
			try:
				message = bot.getMessages(target,min_id)
				break
			except:continue
		for msg in message:
			try:
				if msg["type"]=="Text" and not msg.get("message_id") in list_message_seened:
					print("[" + msg.get("message_id") + "] >>> " + msg["type"] + ">>>" + " " + msg.get("text") + "\n")
					#bot.deleteChatHistory(target,msg.get("message_id"))
					if msg.get('text').startswith('/start'):
						bot.sendMessage(target,'code')
					elif msg.get("text").startswith("link "):
						url =msg.get("text")[5:]
						print(url)
						request.urlretrieve(url,"file.zip")
						print(bot.sendDocument(target,"file.zip"))
						os.remove("file.zip")
					elif msg.get("text").startswith("link1 "):
						url =msg.get("text")[6:]
						gm = requests.get(url)
						with open("file.zip","wb") as f:
							f.write(gm.content)
							print(bot.sendDocument(target,"file.zip"))
				list_message_seened.append(msg.get("message_id"))
			except:continue
		
	except:
		pass