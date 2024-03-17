import requests
import User
from Converter import *

URL = 'https://22dd1f97-419f-4670-90fe-b2048616ab91.mock.pstmn.io'
responce = requests.get(URL+"/User")
responceData = responce.json()
user=User.ParseFromJSON(responceData)
userC=User(user.id,user.name,user.isManager)
print(userC.__dict__)
userII=User.Constructor2(user.id,user.name,user.isManager,email= "yandex")
print(userII.__dict__)