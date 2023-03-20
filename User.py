# User à
# ID
# Nom
# Prenom
# "Pseudo"
# EMAIL
# MDP SHA256
import hashlib
import mysql.connector
from Verification import *

#Ouverture de la base de Données
# dataDiscord = mysql.connector.connect(
# 	host="localhost",
# 	user="root",
# 	password="root",
# 	database="myDiscord"
# 	)

class Utilisateur:

	def __init__(self):
		self.__Nom = ""
		self.__Prenom = ""
		self.__Mail = ""
		self.__MDP = ""
		self.__Pseudo = ""


	def inscription(self, prenom, nom, mail, mdp):
		self.__Nom = nom
		self.__Prenom = prenom
		self.__Mail = mail
		self.__Pseudo = ""
		self.__MDP = ""

		NomCorrect = 0
		PrenomCorrect = 0
		MailCorrect = 0
		MDPCorrect = 0

		if self.__Nom != "":
			NomCorrect = 1
		else:
			NomCorrect = 0

		if mdp != "":
			if motdepasse(mdp) == True:
				self.__MDP = hashlib.sha256(mdp.encode("UTF-8")).hexdigest()
				MDPCorrect = 1
		else:
			MDPCorrect = 0

		if self.__Mail != "":
			MailCorrect = 1
		else:
			MailCorrect = 0

		if self.__Prenom != "":
			PrenomCorrect = 1
		else:
			PrenomCorrect = 0

		if NomCorrect == 1:
			if PrenomCorrect == 1:
				if MailCorrect == 1:
					if MDPCorrect == 1:
						print("Pomme de Terreau")
						# cur = dataDiscord.cursor()
						# cur.execute(f"INSERT INTO user (Nom, Prenom, Mail, MDP) values ('{self.__Nom}', '{self.__Prenom}', '{self.__Mail}', '{self.__MDP}');")
						# dataDiscord.commit()
						# cur.close()



	def connexion(self, mail, mdp):
		self.__MailConnection = mail
		hash = hashlib.sha256(mdp.encode('UTF-8'))
		self.__MDPConnection = hash.hexdigest()

		if self.__MailConnection == self.__Mail:
			if self.__MDPConnection == self.__MDP:
				# return True
				print('tout ok')
			else:
				# return False
				print('mdp pas ok')
		else:
			# return False
			print('adresse pas ok')

	def envoyerMessage(self, message, canal):
		pass


	# def changerPseudo(self):
	# 	self.__Pseudo =


# Test utilisateur
User = Utilisateur()
User.inscription("Matthieu","Geley","Y'apas","AzER*15sZ")
User.connexion("Y'apas","AzER*15sZ")