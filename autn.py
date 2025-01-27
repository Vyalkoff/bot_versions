import requests
import data_for_auth
import parser_updetes
import write_read_html_json


def authorization():
    with requests.Session() as session:
        url_login = data_for_auth.LOGIN_URL
        # Настройка заголовков
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
            'Accept': 'application/json'
        })
        # Получить html для поиска скрытых полей
        response_html = session.get(url_login)
        data = parser_updetes.parser_hidden_auth(response_html)

        # Добавить  пароль и логин
        data['username'] = data_for_auth.LOGIN
        data['password'] = data_for_auth.PASSWORD
        # Авторизоватся
        response_login = session.post(url_login, data=data)

        if response_login.status_code == 200:
            # Записать Cookies в файл
            cookies = [{'name': key.name, 'value': key.value, 'port': key.port,
                        'version': key.version, 'domain': key.domain,
                        'path': key.path} for key in
                       session.cookies]
            result = write_read_html_json.write_for_json('cocke.json', cookies)
            return result


def get_session():
    with requests.Session() as session:
        # result = write_read_html_json.read_out_json('cookies.json')
        coke = write_read_html_json.read_out_json('cocke.json')
        for i in coke:
            session.cookies.set(**i)
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
            'Accept': 'application/json'
        })
        return session


if __name__ == '__main__':
    #authorization()
    session = get_session()
    response = session.get(data_for_auth.ADDRESS_RELEASE)
    print(response.text)
