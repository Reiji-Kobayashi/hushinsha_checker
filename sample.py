from firebase import firebase
from act import main_act
import requests


line_notify_token = '自身のLINEトークン'
line_notify_api = 'https://notify-api.line.me/api/notify'
message = '誰か来ました'

#firebase = firebase.FirebaseApplication("https://iotiot-ae8e8.firebaseio.com/", None)

while(1):
    #result = firebase.get('/Nefry', None)


    #jsonをパースする
    response = input()
    if response == "1":
        #来訪者あり
        mflag = main_act()
        print("来訪者あり")
        if(mflag==1):
            message = '注意：通報リスト該当者が来ました！'
        break
    else:
        #来訪者なし
        print("来訪者なし")


payload = {'message': message}
headers = {'Authorization': 'Bearer ' + line_notify_token}  # 発行したトークン
line_notify = requests.post(line_notify_api, data=payload, headers=headers)


#print(response)
