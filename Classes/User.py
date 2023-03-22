import hashlib
import mysql.connector
from Verification import *
from tkinter import messagebox

#Ouverture de la base de Données
dataDiscord = mysql.connector.connect(
	host="localhost",
	user="root",
	password="root",
	database="myDiscord"
	)

class Utilisateur:

	def __init__(self):
		dataDiscord = mysql.connector.connect(
			host="localhost",
			user="root",
			password="root",
			database="myDiscord"
		)
		self.__Nom = ""
		self.__Prenom = ""
		self.__Mail = ""
		self.__MDP = ""
		self.__Pseudo = ""

	def getData(self):
		cur = dataDiscord.cursor()
		cur.execute(f"SELECT * from utilisateur;")
		AllDATA = cur.fetchall()
		cur.close()
		return AllDATA

	def getID(self, mail):
		cur = dataDiscord.cursor()
		cur.execute(f"SELECT ID from utilisateur where Mail = '{mail}' ;")
		DataID = cur.fetchone()
		cur.close()
		return DataID

	def existence(self, mail):
		data = self.getData()
		for row in data:
			# print(row[4])
			if mail != row[4]:
				print("Mail pas utilisée")
			else:
				# print("Mail utilisé")
				return False

	def inscription(self, prenom, nom, mail, mdp):
		self.__Nom = nom
		self.__Prenom = prenom
		self.__validemail = mail.lower()
		self.__Mail = self.__validemail
		self.__Pseudo = ""
		self.__MDP = ""
		NomCorrect = 0
		PrenomCorrect = 0
		MailCorrect = 0
		MDPCorrect = 0
		print("test")
		if self.existence(self.__validemail) != False:
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
							cur = dataDiscord.cursor()
							cur.execute(f"INSERT INTO utilisateur (Nom, Prenom, Mail, MDP) values ('{self.__Nom}', '{self.__Prenom}', '{self.__Mail}', '{self.__MDP}');")
							dataDiscord.commit()
							cur.close()
		else:
			print("Rien ne se passe")

	def connexion(self, mail, mdp):
		validemail = mail.lower()
		self.__IDconnecte = self.getID(validemail)
		hash = hashlib.sha256(mdp.encode('UTF-8'))
		MDPConnection = hash.hexdigest()
		data = self.getData()
		for row in data:
			if row[4] == validemail and row[5] == MDPConnection:
				return True
			else:
				return False


	def envoyerMessage(self, message, canal):
		print(self.__IDconnecte[0], f"{message}", canal)
		cur = dataDiscord.cursor()
		cur.execute(f"INSERT INTO message (Contenu, ID_Canal, ID_Emetteur) values ('{message}', {canal}, {self.__IDconnecte[0]});")
		dataDiscord.commit()
		cur.close()

	# def changerPseudo(self):
	# 	self.__Pseudo =


# # Test utilisateur
User = Utilisateur()
User.getData()
# User.existence("{rootmail@laplateforme.io}")
# User.inscription("Matthieu","Geley", "matthieu.geley@laplateforme.io","AzER*15sZ")
#User.connexion("matthieu.geley@laplateforme.io","AzER*15sZ")
User.connexion("{rootmail@laplateforme.io}","{root}")
User.envoyerMessage("prout",5)