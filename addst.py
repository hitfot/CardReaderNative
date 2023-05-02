import requests
import urllib
from urllib.request import urlopen
from urllib.request import Request
import json

if __name__ == "__main__":
    print("Для выхода напишите 'cls'")
    try:
        url = 'https://ipelab.ru/serv/atten.php'
        payload = {'py_get_comm' : 1,}
        
        x = requests.get(url, params=payload)
        #print(x.text)
        response = json.loads(x.text)

        StudentsList = {}

        for i in range(0, len(response)):
            #print(response[i]['studak'], response[i]['name'])
            StudentsList.update({response[i]['studak'] : response[i]['name']})

        print('Список студентов получен')
    except:
        print('Ошибка получения списка студентов')


    while(True):
        stn = input()
        if stn != 'cls' and len(stn) > 9:
            #print('st:', stn)
            if stn not in StudentsList:
                try: 
                    studentName = input('Введите ФИО стдуента: ', )
                    studentPassword = input('Придумайте пароль для студента: ', )
                    url = 'https://ipelab.ru/serv/atten.php'
                    payload =   {
                                    'py_post_comm'  : 2,
                                    'studak'        : stn,
                                    'name'          : studentName,
                                    'password'      : studentPassword
                                }
                    
                    x = requests.post(url, data=payload)
                    print(x.text)
                except:
                    print('Ошибка добавления студента')
            else:
                print('Такой студент уже есть')
        else:
            break
