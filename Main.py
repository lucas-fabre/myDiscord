import mysql.connector
from tkinter import *
from tkinter import ttk
from User import *
import hashlib

##---Définition de la fenêtre---##
fenetre = Tk()
fenetre.geometry('200x150')
fenetre.title('myDiscord - Connexion')

#----------"Connexion"----------#

#Mail.
txtmail = Label(fenetre, text = "Adresse mail:")
txtmail.pack()

mail = Entry(fenetre)
mail.pack()

#Mot de passe.
txtmdp = Label(fenetre, text = "Mot de passe:")
txtmdp.pack()

mdp = Entry(fenetre)
mdp.pack()

#----------"Créer un compte"----------#

def ouvrir_creation():
    #Fenêtre "Créer un compte".
    f_creation = Toplevel()
    f_creation.geometry('200x200')

    #Nom.
    txtnom = Label(f_creation, text = "Nom:")
    txtnom.pack()

    nom = Entry(f_creation)
    nom.pack()

    #Prénom.
    txtprenom = Label(f_creation, text = "Prénom:")
    txtprenom.pack()

    prenom = Entry(f_creation)
    prenom.pack()

    #Mail.
    txtmail = Label(f_creation, text = "Adresse mail:")
    txtmail.pack()

    mail1 = Entry(f_creation)
    mail1.pack()

    #Mot de passe.
    txtmdp = Label(f_creation, text = "Mot de passe:")
    txtmdp.pack()

    mdp = Entry(f_creation)
    mdp.pack()

    #Bouton "Valider et créer mon compte".
    validation = Button(f_creation, text = "Valider et créer mon compte", command = User.inscription)
    validation.pack()

#----------"Fenêtre Principale"----------#
# def ouvrir_principale():
#     #Fenêtre principale.
#     f_principale = Toplevel()
#     f_principale.geometry('1200x800')


#     #-----Liste des contacts-----#
    
#     columnC = 'Contacts'
#     tree = ttk.Treeview(fenetre, height = 15, column = columnC, show = 'headings')
#     tree.grid(column = 0, sticky = 'news')

#     #Attributs des colonnes.
#     for col in columnC:
#         tree.heading(col, text=col)
#         tree.column(col, width=100, anchor=CENTER)

#     #Récupération des contacts.
#     cursor.execute("SELECT * FROM user")
#     data =cursor.fetchall()

#     for i in data:
#         tree.insert("", END, values=i)

#     cursor.close()

#     #Scrollbar contacts.
#     sb = Scrollbar(fenetre, orient=VERTICAL, command=tree.yview)
#     sb.grid(row=1, column=1, sticky='ns')
#     tree.config(yscrollcommand=sb.set)

    
#     #-----Zone de discussion-----#
    
#     columnD = 'Discussion'
#     tree = ttk.Treeview(fenetre, height = 15, column = columnD, show = 'headings')
#     tree.grid(column = 0, sticky = 'news')

#     #Attributs des colonnes.
    
#     for col in columnD:
#         tree.heading(col, text=col)
#         tree.column(col, width=100, anchor=CENTER)

#     #Récupération des contacts.
#     cursor.execute("SELECT * FROM ")
#     data =cursor.fetchall()

#     for i in data:
#         tree.insert("", END, values=i)

#     cursor.close()

#     #Scrollbar contacts.
#     sb = Scrollbar(fenetre, orient=VERTICAL, command=tree.yview)
#     sb.grid(row=1, column=1, sticky='ns')
#     tree.config(yscrollcommand=sb.set)


#---Définition des boutons---#

#Bouton "Connexion".
b_connexion = Button(fenetre, text = "Connexion", command = lambda: User.connexion(mail.get(), mdp.get()))
b_connexion.pack()

#Bouton "Créer un compte".
b_creation = Button(fenetre, text = "Créer un compte", command = ouvrir_creation)
b_creation.pack()

fenetre.mainloop()