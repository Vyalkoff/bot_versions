import json

import data_for_auth
import write_read_html_json
from requests_release_path import request_path, request_release

with open("data_release_json/release.json", encoding="utf-8") as file:
    data = json.load(file)


def search_count_version(vers: str):
    len_data = len(data) - 1

    for number in range(len_data):
        for key, value in data[str(number)].items():
            if vers in value['previousVersionsColumn']:
                return key


def last_version(vers: dict):
    for i in data.get('0'):
        return i


def find_version(version):
    last_vers = last_version(data)
    counter = 0
    all_version = []

    while last_vers != version:
        version = search_count_version(version)
        all_version.append(version)
        counter += 1
    return counter, all_version


def find_path_for_last_release(session):
    last_vers = last_version(data)
    address_html = request_path(session, last_vers)
    if address_html:
        write_read_html_json.write_for_json(address_html, data_for_auth.LOCAL_ADDRESS_PATH_JSON)
    else:
        return False


def find_path_for_release(session, release):
    pass
