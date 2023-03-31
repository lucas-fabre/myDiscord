import hashlib
import mysql.connector
from Verification import *
from tkinter import messagebox
from tkinter import ttk
# from Connexion import  *

#Ouverture de la base de Données
dataDiscord = mysql.connector.connect(
	host="localhost",
	user="root",
	password="R00t",
	database="myDiscord"
	)

class Utilisateur:
	def __init__(self):
		dataDiscord = mysql.connector.connect(
			host="localhost",
			user="root",
			password="R00t",
			database="myDiscord"
		)
		self.__Nom = ""
		self.__Prenom = ""
		self.__Mail = ""
		self.__MDP = ""
		self.__Pseudo = ""

	def getData(self):
		curseur = dataDiscord.cursor()
		curseur.execute(f"SELECT * from utilisateur;")
		TouteData = curseur.fetchall()
		curseur.close()
		return TouteData

	def getID(self, mail):
		curseur = dataDiscord.cursor()
		curseur.execute(f"SELECT ID from utilisateur where Mail = '{mail}' ;")
		DataID = curseur.fetchone()
		curseur.close()
		print(DataID)
		return DataID

	def existence(self, mail):
		data = self.getData()
		for ligne in data:
			# print(ligne[4])
			if mail != ligne[4]:
				print("Mail pas utilisée")
		else:
			# print("Mail utilisé")
			return False

	def doublon(self, pseudo):
		data = self.getData()
		for ligne in data:
			# print(ligne[3])
			# print(pseudo)
			if pseudo != ligne[3]:
				print("Pseudo pas utilisée")
		else:
			# print("Pseudo utilisé")
			return False

	def inscription(self, prenom, nom, pseudo, mail, mdp):
		self.__Nom = nom
		self.__Prenom = prenom
		self.__validemail = mail.lower()
		self.__Mail = self.__validemail
		self.__Pseudo = pseudo
		self.__MDP = ""
		NomCorrect = 0
		PrenomCorrect = 0
		MailCorrect = 0
		MDPCorrect = 0
		PseudoCorrect = 0
		# print("test")
		if self.existence(self.__validemail) == False:
			if self.doublon(self.__Pseudo) == False:
				if self.__Nom != "":
					NomCorrect = 1
				else:
					NomCorrect = 0
				if self.__Pseudo != "":
					PseudoCorrect = 1
				else:
					PseudoCorrect = 0
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
					if PseudoCorrect ==1:
						if PrenomCorrect == 1:
							if MailCorrect == 1:
								if MDPCorrect == 1:
									# print("User créer")
									curseur = dataDiscord.cursor()
									curseur.execute(f"INSERT INTO utilisateur (Nom, Prenom, Pseudo, Mail, MDP) values ('{self.__Nom}', '{self.__Prenom}', '{self.__Pseudo}', '{self.__Mail}', '{self.__MDP}');")
									dataDiscord.commit()
									curseur.close()
			else:
				print("Rien ne se fait")
		else:
			print("Rien ne se passe")

	def getMail(self):
		mail = self.validemail

		return mail

	def connexion(self, mail, mdp):
		self.validemail = mail.lower()
		self.mail = self.getMail()
		# print(self.mail , "+1")
		self.IDconnecte = self.getID(self.validemail)
		MDPConnection = hashlib.sha256(mdp.encode('UTF-8')).hexdigest()
		data = self.getData()
		for ligne in data:
			if ligne[4] == self.validemail and ligne[5] == MDPConnection:
				# print("connecté")
				self.IDconnecte = ligne[0]
				# print(self.IDconnecte, "+1")
				return True
		else:
			return False


	def envoyerMessage(self, message, canal):
		f = open("ID.txt", "r")
		self.__ID = f.read()
		strmessage = str(message)
		# print(self.IDconnecte[0], f"{message}", canal)
		# IDemetteur = self.getID(self.getMail())
		curseur = dataDiscord.cursor()
		curseur.execute(f'INSERT INTO message (Contenu, ID_Canal, ID_Emetteur) values ("{strmessage}", "{canal}", "{self.__ID}");')
		dataDiscord.commit()
		curseur.close()
		# print(message, canal)

	def changerPseudo(self, pseudo):
		self.__Pseudo = pseudo
		PseudoCorrect = 0
		if self.doublon(self.__Pseudo) != False:
			if self.__Pseudo != "":
				PseudoCorrect = 1
			else:
				PseudoCorrect = 0
				if PseudoCorrect == 1:
					curseur = dataDiscord.cursor()
					curseur.execute(f"UPDATE utilisateur SET Pseudo = '{self.__Pseudo}' where ID = {self.__ID};")
					dataDiscord.commit()
					curseur.close()


# # Test utilisateur
User = Utilisateur()
User.getData()
# User.existence("{rootmail@laplateforme.io}")
# User.inscription("Matthieu","Geley", "matthieu.geley@laplateforme.io","AzER*15sZ")
# User.inscription("Test2", "Test2", "ADMINISTRATEUR","tes2t.test@laplateforme.io", "AzER*15sZ")
# User.connexion("test.test@laplateforme.io", "AzER*15sZ")

# User.connexion("matthieu.geley@laplateforme.io","AzER*15sZ")
# User.connexion("{rootmail@laplateforme.io}","{root}")
# User.envoyerMessage("prout",5)
# User.changerPseudo("ADMINISTRATEUR")