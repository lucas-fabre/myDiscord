# Chat à
# ID
# Nom
# Status: 1 = public; 0 =privé,


class Communication:

	def __init__(self):
		pass

	def visibilite(self, status):
		if status == 1:
			self.__visible = 1
		else:
			self.__visible = 0
