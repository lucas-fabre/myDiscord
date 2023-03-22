class Communication:

	def __init__(self, id, nom, message, IDU):
		self.__ID = id
		self.__Nom = nom
		self.__visible = "0"
		self.__message = message
		self.__IDUtilisateur = IDU

	def visibilite(self, status):
		if status == 1:
			self.__visible = 1
		else:
			self.__visible = 0
		if self.__visible == 1:
			if etat_utilisateur >= 1:
				print("showing canal")