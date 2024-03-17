import Converter

class User():
	def __init__(self,id,name,isManager):
		self._id = id
		self._name = name
		self._isManager = isManager

	@classmethod
	def ParseFromJSON(self,JsonObject):
		return Converter.ConvertJSONToclass(JsonObject,objectName=User)
	@classmethod
	def Constructor2(cls,id,name,isManager,email):
		user=User(id,name,isManager)
		user.email=email
		return user
