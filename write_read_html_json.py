import requests_release_path
import logging
import autn
import data_for_auth
import json

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")


# requests_release_path.request_path(release="3.0.60.1")


def write_for_html(address, html_response):
    try:
        with open(address, 'w', encoding='utf-8') as file:
            file.write(html_response.text)
        return True
    except FileNotFoundError:
        logging.exception("Не правильный путь")
        return False


def read_out_html(address):
    with open(address, encoding='utf-8') as file:
        return file.read()


def write_for_json(address_json, result, type_data=None):
    try:
        with open(address_json, "w", encoding="utf-8") as file:
            json.dump(result, file)
        return True
    except FileNotFoundError:
        logging.exception("Не правильный путь")
        return False


def read_out_json(address):
    with open(address, encoding="utf-8") as file:
        return json.load(file)


if __name__ == '__main__':
    pass
# if write_for_html(data_for_auth.LOCAL_ADDRESS_PATH_HTML,
#                   requests_release_path.request_path(autn.authorization())):
#     print("файл HTML Записан")
