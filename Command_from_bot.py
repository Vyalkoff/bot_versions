import requests_release_path
import search_version
import parser_updetes
import write_read_html_json
import data_for_auth
import autn


def update_release():
    session = autn.get_session()
    response = requests_release_path.request(session, data_for_auth.ADDRESS_RELEASE)
    versions_dict = parser_updetes.parser_release(session, response.text, True)
    record = write_read_html_json.write_for_json(data_for_auth.LOCAL_ADDRESS_RELEASE_AND_LINK_JSON, versions_dict)
    if record:
        return "Информация о релизах обновлена"
    else:
        return "Возникла ошибка обратится к VLAD"


def check_new_release():
    session = autn.get_session()
    response = requests_release_path.request(session, data_for_auth.ADDRESS_RELEASE)
    versions_dict_site = parser_updetes.parser_release(session, response.text, False)
    last_version_site = search_version.last_version(versions_dict_site)
    versions_dict_file = write_read_html_json.read_out_json(data_for_auth.LOCAL_ADDRESS_RELEASE_JSON)
    last_version_json = search_version.last_version(versions_dict_file)
    if last_version_json != last_version_site:
        recorded = update_file_release(versions_dict_site, versions_dict_file)
        if recorded:
            return f"Вышел новый релиз {last_version_site}. Информация обновлена!"
        else:
            return f"Произошла ошибка. Обратится к администратору"
    else:
        return f'Последняя версия {last_version_json}'


def update_file_release(versions_dict_site, versions_dict_file):
    number = 0
    for value in versions_dict_file.values():
        versions_dict_site[number + 1]: value
    return write_read_html_json.write_for_json(data_for_auth.LOCAL_ADDRESS_RELEASE_JSON, versions_dict_site)


# def check_new_path(session):
#     data = write_read_html_json.read_out_json(data_for_auth.LOCAL_ADDRESS_RELEASE_JSON)
#     last_version_json = search_version.last_version(data)
#     address_html = requests_release_path.request_path(session,last_version_json)
#     if address_html:
#         # versions_on_site = parser_updetes.parser_release(35)
#         # last_version_site = search_version.last_version(versions_on_site)
#         # data = write_read_html_json.read_out_json(data_for_auth.LOCAL_ADDRESS_RELEASE_JSON)
#         # last_version_json = search_version.last_version(data)
#     #     if last_version_json != last_version_site:
#     #         recorded = write_read_html_json.write_for_json(data_for_auth.LOCAL_ADDRESS_RELEASE_JSON, versions_on_site)
#     #         if recorded:
#     #             return f"Вышел новый релиз {last_version_site}. Информация Обновлена"
#     #         else:
#     #             return f"Произошла ошибка. Обратится к администратору"
#     #     else:
#     #         return f'Последняя версия {last_version_json}'
#      else:
#          return f"Произошла ошибка. Обратится к администратору"

def update_path():
    session = autn.get_session()
    data_release = write_read_html_json.read_out_json(data_for_auth.LOCAL_ADDRESS_RELEASE_JSON)
    last_version = search_version.last_version(data_release)
    response = requests_release_path.request_path(session, last_version)
    data_path = parser_updetes.parser_path(response.text)
    data = {last_version: data_path}
    recorded = write_read_html_json.write_for_json(data_for_auth.LOCAL_ADDRESS_PATH_JSON, data)
    if recorded:
        return data
    else:
        return False


if __name__ == '__main__':
    print(update_path())
