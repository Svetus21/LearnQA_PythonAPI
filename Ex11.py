import requests

def test_cookie():
    url = "https://playground.learnqa.ru/api/homework_cookie"
    response = requests.get(url)
    print(response.cookies)
    assert "HomeWork" in response.cookies, "There is no cookie 'HomeWork' in the response"
    assert response.cookies["HomeWork"] == "hw_value", "Cookie 'HomeWork' value is wrong"