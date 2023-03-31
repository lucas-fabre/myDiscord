import mysql.connector
import os
from tkinter import *
from tkinter import ttk
import User

dataDiscord = mysql.connector.connect(
	host="localhost",
	user="root",
	password="R00t",
	database="myDiscord"
	)

class Main:
    def __init__(self):
        dataDiscord = mysql.connector.connect(
        host="localhost",
        user="root",
        password="R00t",
        database="myDiscord"
        )

        cur = dataDiscord.cursor(buffered= True)

        self.f_principale = Tk()
        self.f_principale.geometry('1000x675')
        self.f_principale.title('myDiscord')

        connecter = Label(self.f_principale, text = User.connexion)
        connecter.pack(side = TOP)
        #----------Partie "Contacts"----------#
        l_contacts = Frame(self.f_principale)
        l_contacts.pack(side = LEFT)

        #label "Contacts".
        lblcontacts = Label(l_contacts, text = "Contacts")
        lblcontacts.pack()

        #Tableau.
        columns = ('Nom', 'Prenom')
        tree_contacts = ttk.Treeview(l_contacts, height = 30, columns = columns, show = 'headings')
        tree_contacts.pack(side = LEFT)

        #Attributs des colonnes
        for col in columns:
            tree_contacts.heading(col, text = col)
            tree_contacts.column(col, width = 100, anchor = CENTER)

        #Récupération des infos.
        cur.execute("SELECT Nom, Prenom FROM utilisateur")
        data =cur.fetchall()

        for i in data:
            tree_contacts.insert("", END, values = i)

        #Scrollbar
        sb = Scrollbar(l_contacts, orient = VERTICAL, command = tree_contacts.yview)
        sb.pack(side = LEFT, fill = "y")
        tree_contacts.config(yscrollcommand = sb.set)

        #----------Fin partie "Contacts"----------#

        Main.canaux(self)
        Main.chat(self)
        
        #----------Partie "Canaux"----------#
    def canaux(self):
        l_canaux = Frame(self.f_principale)
        l_canaux.pack(side = LEFT)

        cur = dataDiscord.cursor(buffered= True)

        #label "Canaux".
        lblcanaux = Label(l_canaux, text = "Discussions")
        lblcanaux.pack()

        #---Frame où l'affichage des canaux et la barre de scroll seront groupés.---#
        zone_canaux = Frame(l_canaux)
        zone_canaux.pack()

        #Affichage des canaux.
        columns = ('Salons', 'Type')
        self.tree_canaux = ttk.Treeview(zone_canaux, height = 29, columns = columns, show = 'headings')
        self.tree_canaux.pack(side = LEFT)

        #Attributs des colonnes
        for col in columns:
            self.tree_canaux.heading(col, text = col)
            self.tree_canaux.column("Salons", width = 100, anchor = CENTER)
            self.tree_canaux.column("Type", width = 100, anchor = CENTER)

        #Récupération des infos.
        cur.execute("SELECT Nom, Type FROM Canaux")
        data = cur.fetchall()

        for i in data:
            self.tree_canaux.insert("", END, values = i)

        #Scrollbar
        sb = Scrollbar(zone_canaux, orient = VERTICAL, command = self.tree_canaux.yview)
        sb.pack(side = LEFT, fill = "y")
        self.tree_canaux.config(yscrollcommand = sb.set)

        #Bouton "Se connecter".
        b_connecter = Button(l_canaux, text = "Se connecter", command = self.selection)
        b_connecter.pack(side = RIGHT)

        #----------Fin partie "Canaux"----------#

    #Méthode permettant de sélectionner un canal pour s'y connecter et de rafraichir l'affichage des messages envoyés dans ce dernier.
    def selection(self):
        select_canal = self.tree_canaux.focus()
        details = self.tree_canaux.item(select_canal)
        Nom = details.get("values")[0]     
        curseur = dataDiscord.cursor(buffered= True)
        curseur.execute(f"SELECT ID from canaux where Nom = '{Nom}';")
        self.ID_canal = curseur.fetchone()

        dataDiscord.commit()

        for item in self.tree_messages.get_children():
            self.tree_messages.delete(item)
            curseur.execute(f"SELECT prenom, contenu FROM message inner join utilisateur on id_emetteur = utilisateur.id where ID_canal = '{self.ID_canal[0]}'")
            data =curseur.fetchall()

        for i in data:
            self.tree_messages.insert("", END, values=i)

        print(self.ID_canal[0])
        return self.ID_canal[0]


    #----------Partie "Chats textuel"----------#
    def chat(self):
        l_chat = Frame(self.f_principale)
        l_chat.pack(side = LEFT)

        cur = dataDiscord.cursor(buffered= True)

        #label "Nom canal".
        lblchat = Label(l_chat, text = "#Nom du canal")
        lblchat.pack()

        #---Frame où l'affichage du chat et la barre de scroll seront groupés.---#
        zone_texte = Frame(l_chat)
        zone_texte.pack()

        #Affichage des messages du chat.
        columns = ('Emetteur', 'Message')
        self.tree_messages = ttk.Treeview(zone_texte, height = 29, columns = columns, show = 'headings')
        self.tree_messages.pack(side = LEFT)

        #Attributs des colonnes
        for col in columns:
            self.tree_messages.heading(col, text = col)
            self.tree_messages.column('Emetteur', width = 100, anchor = CENTER)
            self.tree_messages.column('Message', width = 400, anchor = CENTER)

        #Récupération des infos.
        cur.execute("SELECT prenom, contenu FROM message inner join utilisateur on id_emetteur = utilisateur.id")
        data = cur.fetchall()

        for i in data:
            self.tree_messages.insert("", END, values = i)

        #Scrollbar
        sb = Scrollbar(zone_texte, orient = VERTICAL, command = self.tree_messages.yview)
        sb.pack(side = LEFT, fill = "y")
        self.tree_messages.config(yscrollcommand = sb.set)

        #---Fin frame où l'affichage du chat et la barre de scroll seront groupés.---#

        #Entrée permettant la saisie du message à envoyer.
        self.entree_texte = Entry(l_chat)
        self.entree_texte.pack(side = LEFT, expand = True, fill = "x")
        #Bouton "Envoie".
        b_envoie = Button(l_chat, text = "Envoyer", command = self.actualiser_messages)
        b_envoie.pack(side = RIGHT)

        self.f_principale.mainloop()
        os.remove("ID.txt")

    #Méthode permettant l'envoie du message rentré dans l'entrée au-dessus en récuperant ce dernier et l'ID du canal pour identifier dans quel canal le message doit être envoyé.
    #Elle permet aussi de rafraichir l'affichage à chaque entrée de texte.
    def actualiser_messages(self):
        cur = dataDiscord.cursor(buffered= True)

        print("ID canal dans actualiser", self.ID_canal[0])
        User.envoyerMessage(self, self.entree_texte.get(), self.ID_canal[0])
        # print(User.envoyerMessage(self.entree_texte.get(), self.ID_canal[0]))

        dataDiscord.commit()

        for item in self.tree_messages.get_children():
            self.tree_messages.delete(item)

            cur.execute(f"SELECT prenom, contenu FROM message inner join utilisateur on id_emetteur = utilisateur.id where ID_canal = '{self.ID_canal[0]}'")
            data =cur.fetchall()

        for i in data:
            self.tree_messages.insert("", END, values=i)

        cur.close()
        #----------Fin partie "Chats textuel"----------#

        

User = User.Utilisateur

# principale = Main()
# principale.canaux()
# principale.chat()
