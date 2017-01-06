import os
import sys
import json
import urllib2
import vk_auth

os.system("clear")

application_id = "4925051"#My is 4925051
login = raw_input(u"Enter your login: ")
password = raw_input(u"Enter your pass: ")

class Connect:
	def __init__(self,application_id,login,password):
		self.access_token = vk_auth.auth(login, password, application_id, "offline,messages")[0]
		print(self.access_token)
		self.layer = ""
		self.uid = ""
		self.section = ""

	def dialog(self, uid=False):
		if uid != self.uid and uid:
			self.uid = uid
		self.layer = ""
		self.section = "dialog"
		dialog = json.loads(urllib2.urlopen("https://api.vk.com/method/messages.getHistory?count=20&user_id=%s&access_token=%s&v=5.33" % (self.uid, self.access_token)).read().decode("utf-8"))
		for item in reversed(dialog["response"]["items"]):
			user = json.loads(urllib2.urlopen("https://api.vk.com/method/users.get?user_id=%s&fields=contacts&access_token%s&v=5.8" % (item["from_id"],self.access_token)).read().decode("utf-8"))["response"][0];
			self.layer+= "%s %s (%s):\n" % (user["first_name"], user["last_name"], item["user_id"])
			self.layer+= "%s \n" % item["body"]
			self.layer+= "-------------------------------------------- \n"

	def dialogs(self):
		self.layer = ""
		self.section = "dialogs"
		dialogs = json.loads(urllib2.urlopen("https://api.vk.com/method/messages.getDialogs?count=50&access_token=%s&v=5.33" % (self.access_token)).read().decode("utf-8"))
		for item in reversed(dialogs["response"]["items"]):
			user = json.loads(urllib2.urlopen("https://api.vk.com/method/users.get?user_id=%s&fields=contacts,online&access_token%s&v=5.8" % (item["message"]["user_id"],self.access_token)).read().decode("utf-8"))["response"][0];
			if (user["online"] == 1):
				user["online"] = "online"
			else:
				user["online"] = "offline"
			self.layer+= "%s %s [%s] (%s):\n" % (user["first_name"], user["last_name"], user["online"], item["message"]["user_id"])
			self.layer+= "%s \n" % item["message"]["body"]
			self.layer+= "--------------------------------------------\n"	
			
	def helpinfo(self):
		print("Input <d> to view all your dialogs")
		print("Input <r> to reload")
		print("Input id from brackets to open a dialog with id-helder\nThen write your messages aand send them with Enter button")
		print("Input <exit> to exit")

	def send(self, message):
		message = urllib2.quote(message).encode('utf8')
		dialog = json.loads(urllib2.urlopen("https://api.vk.com/method/messages.send?user_id=%s&message=%s&access_token=%s&v=5.33" % (self.uid, message, self.access_token)).read().decode("utf-8"))
		self.controll("r")

	def controll(self, input):
		print ("------------====LOADING====------------")
		if input == "d":
			self.dialogs()
		elif input == "help":
			self.helpinfo()
		elif input == "exit":
			os.system("clear")
			sys.exit(0)
		elif input == "":
			self.layer = ""
		elif self.section == "dialogs":
			if input == "r":
				self.dialogs()
			else:
				self.dialog(input)
		elif self.section == "dialog":
			if input == "r":
				self.dialog()
			else:
				self.send(input)
		os.system("clear")
		print (self.layer)
		
		self.controll("%s" % raw_input("Enter command: \n "))


vk = Connect(application_id,login,password)
vk.controll("") 
