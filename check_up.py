import requests_release_path
import search_version
import parser_updetes
import write_read_html_json
import data_for_auth


def check_new_release(session):
    address_html = requests_release_path.request_release(session)
    if address_html:
        versions_on_site = parser_updetes.parser_release()
        last_version_site = search_version.last_version(versions_on_site)
        data = write_read_html_json.read_out_json(data_for_auth.LOCAL_ADDRESS_RELEASE_JSON)
        last_version_json = search_version.last_version(data)
        if last_version_json != last_version_site:
            recorded = write_read_html_json.write_for_json(data_for_auth.LOCAL_ADDRESS_RELEASE_JSON, versions_on_site)
            if recorded:
                return f"Вышел новый релиз {last_version_site}. Информация Обновлена"
            else:
                return f"Произошла ошибка. Обратится к администратору"
        else:
            return f'Последняя версия {last_version_json}'
    else:
        return f"Произошла ошибка. Обратится к администратору"


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

def update_path(session):
    data_release = write_read_html_json.read_out_json(data_for_auth.LOCAL_ADDRESS_RELEASE_JSON)
    last_version = search_version.last_version(data_release)
    address_html = requests_release_path.request_path(session, last_version)
    data_path = parser_updetes.parser_path(address_html)
    data = {last_version: data_path}
    recorded = write_read_html_json.write_for_json(data_for_auth.LOCAL_ADDRESS_PATH_JSON, data)
    if recorded:
        return True
    else:
        return False


if __name__ == '__main__':
    import autn

    print(check_new_release(autn.authorization()))
