from firebase import firebase
from act import main_act
import requests



#yxox0zzREiJiY6ArWwv56hxZbCjyERs9l3eABo4woyx
line_notify_token = 'yxox0zzREiJiY6ArWwv56hxZbCjyERs9l3eABo4woyx'
line_notify_api = 'https://notify-api.line.me/api/notify'
message = '誰か来ました'

firebase = firebase.FirebaseApplication("https://iotiot-ae8e8.firebaseio.com/", None)

while(1):
    result = firebase.get('/Nefry', None)

    #jsonをパースする
    response = result["SW"]
    if response == "1":
        #来訪者あり
        main_act()
        #print("来訪者あり")
        break
    else:
        #来訪者なし
        print("来訪者なし")


payload = {'message': message}
headers = {'Authorization': 'Bearer ' + line_notify_token}  # 発行したトークン
line_notify = requests.post(line_notify_api, data=payload, headers=headers)


#print(response)
