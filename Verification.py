import hashlib
import json

#mot de passe:
#doit contenir 8 caractères
#1 Majuscule
#1 minuscule
#1 chiffre
#1 caractère spécial (!, @, #, $, %, ^, &, *)



def longueur(mdp):
	if len(mdp) >= 8:
		return True


def chiffres(mdp):
	chiffre = "0123456789"
	for i in mdp:
		if i in chiffre:
			return True


def majuscule(mdp):
	majuscule = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i in mdp:
		if i in majuscule:
			return True


def minuscule(mdp):
	minuscule = "abcdefghijklmnopqrstuvwxyz"
	for i in mdp:
		if i in minuscule:
			return True


def speciale(mdp):
	ponctuation = "!@#$%^&*"
	for i in mdp:
		if i in ponctuation:
			return True


def verification(mdp):
	i = 0
	for i in mdp:
		if longueur(mdp) == True and minuscule(mdp) == True and majuscule(mdp) == True and speciale(mdp) == True:
			print("Tout fonctionne comme prévu")
			return True


def motdepasse(motdepass):
	verification = False
	while verification != True:
		mdp = str(motdepass)

		if longueur(mdp) == True and minuscule(mdp) == True and majuscule(mdp) == True and speciale(mdp) == True and chiffres(mdp) == True:
			verification = True
		else:
			print("ERREUR CRITIQUE MDP VERIF")
			break
		if verification == True:
			Sha = hashlib.sha256(mdp.encode("UTF-8")).hexdigest()
			return True