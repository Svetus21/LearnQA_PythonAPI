import requests

def test_headers():
    url = "https://playground.learnqa.ru/api/homework_header"
    response = requests.get(url)
    print(response.headers)
    assert "x-secret-homework-header" in response.headers, "There is no secret header in the response"
    assert response.headers["x-secret-homework-header"] == "Some secret value", "Secret header value is wrong"

