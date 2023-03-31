import mysql.connector
from tkinter import *
from tkinter import ttk
# from User import *
import hashlib
import User

dataDiscord = mysql.connector.connect(
	host="localhost",
	user="root",
	password="R00t",
	database="myDiscord"
	)

class Creation_compte:
    def __init__(self):
        #Fenêtre "Créer un compte".
        f_creation = Toplevel()
        f_creation.geometry('200x250')

        #Prénom.
        txtprenom = Label(f_creation, text = "Prénom:")
        txtprenom.pack()

        prenom = Entry(f_creation)
        prenom.pack()

        #Nom.
        txtnom = Label(f_creation, text = "Nom:")
        txtnom.pack()

        nom = Entry(f_creation)
        nom.pack()

        #Pseudo.
        txtpseudo = Label(f_creation, text = "Pseudo:")
        txtpseudo.pack()

        pseudo = Entry(f_creation)
        pseudo.pack()

        #Mail.
        txtmail = Label(f_creation, text = "Adresse mail:")
        txtmail.pack()

        mail = Entry(f_creation)
        mail.pack()

        #Mot de passe.
        txtmdp = Label(f_creation, text = "Mot de passe:")
        txtmdp.pack()

        mdp = Entry(f_creation)
        mdp.pack()

        #Bouton "Valider et créer mon compte".
        validation = Button(f_creation, text = "Valider et créer mon compte", command = lambda: User.inscription(prenom.get(), nom.get(), pseudo.get(), mail.get(), mdp.get()))
        validation.pack()

        f_creation.mainloop


User = User.Utilisateur()
compte = Creation_compte