import time

import autn
import data_for_auth
import write_read_html_json


def request(session, address):
    response = session.get(address, timeout=5)
    if response.status_code == 200:
        return response
    else:
        return False
    # recorded = write_read_html_json.write_for_html(data_for_auth.LOCAL_ADDRESS_RELEASE_HTML, response_updates)


def request_path(session, release):
    address_path = data_for_auth.ADDRESS_PATH + release
    response_updates = session.get(address_path)
    if response_updates.status_code == 200:
        return response_updates
    else:
        return False


if __name__ == '__main__':
    pass
    # if request_path(autn.authorization(), "3.0.62.1"):
    #     print("файл html получен")
    # else:
    #     print("Произошла Ошибка")
