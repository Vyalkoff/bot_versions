import requests
from bs4 import BeautifulSoup
import data_for_auth


def authorization():
    url_login = "https://login.1c.ru/login?service=https%3A%2F%2Fportal.1c.ru%2Fpublic%2Fsecurity_check"

    with requests.Session() as session:

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
            di = [{'name': key.name, 'value': key.value, 'port': key.port, 'version': key.version, 'domain': key.domain,
                   'path': key.path} for key in
                  session.cookies]
            write_read_html_json.write_for_json('cocke.json',di)


            print(di)


            # data = requests.utils.dict_from_cookiejar(session.cookies)
            # write_read_html_json.write_for_json('cookies.json', result=data)
        with requests.Session() as s:
            # result = write_read_html_json.read_out_json('cookies.json')
            coke = write_read_html_json.read_out_json('cocke.json')
            print(coke)
            for i in coke:
                s.cookies.set(**i)
            s.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
                'Accept': 'application/json'
            })
            print(s.cookies)
            response = s.get(data_for_auth.ADDRESS_RELEASE)
            print(response.text)


if __name__ == '__main__':
    import requests
    import json
    import write_read_html_json
    import data_for_auth

    authorization()
    # result = write_read_html_json.read_out_json('cookies.json')
    # with requests.Session() as s:
    #     print(s.get(data_for_auth.ADDRESS_RELEASE,cookies=result).text)
