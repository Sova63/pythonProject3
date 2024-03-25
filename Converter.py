from collections import namedtuple
from User import User

def ConvertJSONToClass(jsonObject,objectName):
	obj = namedtuple(objectName.jsonObject.keys())(*jsonObject.value())
	return obj
def ConvertUserJSONToClass(jsonObject):
	return User(jsonObject["id"],jsonObject["name"],jsonObject["isManager"])

# Converter.py
"""
import json

def ConvertJSONToClass(json_data, objectName):
	data = json.loads(json_data)
	obj = object()
	for key, value in data.items():
		setattr(obj, key, value)
	return obj

"""