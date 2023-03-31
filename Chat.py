import hashlib
import mysql.connector
from Verification import *
from tkinter import messagebox

dataDiscord = mysql.connector.connect(
	host="localhost",
	user="root",
	password="root",
	database="myDiscord"
)

class Communication:

	def __init__(self):
		self.__Nom = ""

	def creerCanal(self, nom):
		self.__Nom = nom
		statut = 1
		curseur = dataDiscord.cursor()
		curseur.execute(f"INSERT INTO textuel (Nom_CT, Status) values ('{self.__Nom}', {statut});")
		dataDiscord.commit()
		curseur.close()

	def afficherMessage(self):
		curseur = dataDiscord.cursor()
		curseur.execute(f"SELECT Pseudo, Contenu FROM utilisateur INNER JOIN message ON utilisateur.id = message.ID_Emetteur;")
		dataDiscord.commit()
		curseur.close()

Chat = Communication()
# Chat.creerCanal("Generale")
# Chat.creerCanal("Aide")