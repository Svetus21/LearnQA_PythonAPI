import requests

#1
print('1: http-запрос любого типа без параметра method')
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print('Ответ:', response.text,'\n')

#2
print('2: http-запрос с методом не из списка')
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": 'HEAD'})
print('Ответ:', response.text,'\n')

#3
print('3: запрос с правильным значением method')
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": 'POST'})
print('Ответ:', response.text,'\n')

#4
print('4: В каких случаях запрос отрабатывает неправильно')
URL = "https://playground.learnqa.ru/ajax/api/compare_query_type"
methods = ['POST', 'GET', 'PUT', 'DELETE']
for method in methods:
    functions = {
        'POST': requests.post(URL, data={"method": method}),
        'GET': requests.get(URL, params={"method": method}),
        'PUT': requests.put(URL, data={"method": method}),
        'DELETE': requests.delete(URL, data={"method": method}),
    }
    for method1 in methods:
        response_text = functions[method1].text
        if response_text != 'Wrong method provided' and method != method1:
            print('Тип запроса не совпадает со значением параметра, но сервер отвечает, что все ок:\n'
                  'Тип запроса:', method1, '\nЗначение параметра method:', method, '\nОтвет: ', response_text)
        elif response_text == 'Wrong method provided' and method == method1:
            print('Тип запроса и значение параметра совпадают, но сервер считает, что это не так:\n'
                  'Тип запроса:', method1, '\nЗначение параметра method:', method, '\nОтвет: ', response_text)

