import requests
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job").json()
seconds = response["seconds"]
token = response["token"]
print('На выполнение задачи понадобится', seconds,'секунд. Токен:', token)

response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token}).json()
if "error" in response1:
    print('Возникла ошибка:', response1["error"])
else:
    if response1["status"] == 'Job is NOT ready':
        print('Статус до выполнения задачи правильный:', response1["status"])
    else:
        print('Статус до выполнения задачи неправильный:', response1["status"])

    time.sleep(seconds)

    response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token}).json()

    if "error" in response2:
        print('Возникла ошибка:', response2["error"])
    else:
        if "result" in response2:
            print('Задача выполнена. Результат:', response2["result"])
            if response2["status"] == 'Job is ready':
                print('Статус после выполнения задачи правильный:', response2["status"])
            else:
                print('Статус после выполнения задачи неправильный:', response2["status"])
        else:
            print('Задача не выполнена, хотя указанное время прошло')




