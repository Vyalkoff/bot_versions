import requests
from bs4 import BeautifulSoup
import data_for_auth




def authorization():
    url_login = "https://login.1c.ru/login?service=https%3A%2F%2Fportal.1c.ru%2Fpublic%2Fsecurity_check"

    session = requests.Session()

    # Настройка заголовков
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
        'Accept': 'application/json'
    })

    response = session.get(url_login)
    soup = BeautifulSoup(response.text, "html.parser")

    hidden_inputs = soup.find_all("input", type="hidden")
    data = {}
    for input_tag in hidden_inputs:
        data[input_tag.get("name")] = input_tag.get("value")

    data['username'] = data_for_auth.LOGIN
    data['password'] = data_for_auth.PASSWORD

    response_login = session.post(url_login, data=data)

    if response_login.status_code == 200:
        return session
    else:
        return False


if __name__ == '__main__':
    if authorization():
        print("Авторизован")
    else:
        print("Не авторизован")
