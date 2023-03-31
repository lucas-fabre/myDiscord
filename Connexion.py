import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Creation
import User
import Main

dataDiscord = mysql.connector.connect(
	host="localhost",
	user="root",
	password="R00t",
	database="myDiscord"
	)

class Connexion:
    def __init__(self):
        self.f_connexion = Tk()
        self.f_connexion.geometry('200x150')
        self.f_connexion.title('myDiscord - Connexion')

        #Mail.
        txtmail = Label(self.f_connexion, text = "Adresse mail:")
        txtmail.pack()

        self.mail = Entry(self.f_connexion)
        self.mail.pack()
                
        #Mot de passe.
        txtmdp = Label(self.f_connexion, text = "Mot de passe:")
        txtmdp.pack()

        self.mdp = Entry(self.f_connexion)
        self.mdp.pack()

        #Bouton "Connexion".
        b_connexion = Button(self.f_connexion, text = "Connexion", command = self.changement_fenetre)
        b_connexion.pack()

        #Bouton "Créer un compte".
        b_creation = Button(self.f_connexion, text = "Créer un compte", command = Creation.Creation_compte)
        b_creation.pack()

        self.f_connexion.mainloop()

    def getMail(self):
        mail = self.mail.get()

        return mail

    def m_erreur(self, mail, mdp):
        if User.connexion(mail, mdp) == True:
            return True
            
        else:
            messagebox.showinfo("Erreur !", "L'adresse mail ou le mot de passe est incorrect")

    def changement_fenetre(self):
        if self.m_erreur(self.mail.get(), self.mdp.get()) == True:

            f = open("ID.txt", "w")
            f.write(f"{User.IDconnecte}")
            f.close()
            self.f_connexion.destroy()
            Main.Main()

        else:
            print("pas changement")

User = User.Utilisateur()
debut = Connexion()