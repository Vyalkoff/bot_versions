import autn
import data_for_auth
import write_read_html_json


def request_release(session, release=False):
    address_release = data_for_auth.ADDRESS_RELEASE
    response_updates = session.get(address_release)
    recorded = write_read_html_json.write_for_html(data_for_auth.LOCAL_ADDRESS_RELEASE_HTML, response_updates)
    if recorded:
        return data_for_auth.LOCAL_ADDRESS_RELEASE_HTML
    else:
        return False


def request_path(session, release):
    address_path = data_for_auth.ADDRESS_PATH + release

    response_updates = session.get(address_path)

    recorded = write_read_html_json.write_for_html(data_for_auth.LOCAL_ADDRESS_PATH_HTML, response_updates)
    if recorded:
        return data_for_auth.LOCAL_ADDRESS_PATH_HTML
    else:
        return False


if __name__ == '__main__':
    if request_path(autn.authorization(), "3.0.62.1"):
        print("файл html получен")
    else:
        print("Произошла Ошибка")
