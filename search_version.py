#!/usr/bin/python
# -*- coding: utf-8 -*-


import json

import data_for_auth
import write_read_html_json
from requests_release_path import request_path, request

with open("data_release_json/release_link.json", encoding="utf-8") as file:
    data = json.load(file)


def search_count_version(vers: str):
    len_data = len(data) - 1

    for number in range(len_data):
        for key, value in data[str(number)].items():
            if vers in value['previousVersionsColumn']:
                return key, value['links_release']


def last_version(vers: dict):
    for i in data.get('0'):
        return i


def find_version(version):
    last_vers = last_version(data)
    counter = 0
    all_version = {}

    while last_vers != version:
        version, links = search_count_version(version)
        all_version[version] = links
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


if __name__ == '__main__':
    counter, all_version = find_version('3.0.50.1')
    release = ""
    for links in all_version:
        # content = TextLink(links, url=all_version[links][0])
        # release += content
        release += release + f'<a href={all_version[links][0]}>{links}</a>'
    text = f'С версии 3.0.50.1 До последней версии {counter}\n Релизы {release}'
    print(text)
