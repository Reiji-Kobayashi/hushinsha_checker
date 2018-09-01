from firebase import firebase
from main import main_act
import requests

firebase = firebase.FirebaseApplication("https://iotiot-ae8e8.firebaseio.com/", None)
result = firebase.get('/Nefry', None)

#yxox0zzREiJiY6ArWwv56hxZbCjyERs9l3eABo4woyx
line_notify_token = 'yxox0zzREiJiY6ArWwv56hxZbCjyERs9l3eABo4woyx'
line_notify_api = 'https://notify-api.line.me/api/notify'
message = '誰か来ました'

#jsonをパースする
response = result["SW"]

if response == "1":
    #来訪者あり
    main_act()
    #print("来訪者あり")
else:
    #来訪者なし
    print("来訪者なし")


payload = {'message': message}
headers = {'Authorization': 'Bearer ' + line_notify_token}  # 発行したトークン
line_notify = requests.post(line_notify_api, data=payload, headers=headers)


#print(response)
