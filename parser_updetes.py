#!/usr/bin/python
# -*- coding: utf-8 -*-
import autn
import requests_release_path
import write_read_html_json
from bs4 import BeautifulSoup
import data_for_auth
import time


# def create_dict(**qwargs):
#     d = {k: v for k, v in qwargs.items()}
#     return d


# table = soup.find('table', {'id': "versionsTable"}).find('tbody').find_all('tr')


def find_versions(session,soup):
    number = 0
    data = {}

    find_all_in_table = soup.find('table', {'id': "versionsTable"}).find('tbody').find_all('tr')
    formatted_time = time.ctime(time.time())
    print(f"Начало сбора ниформации {formatted_time}")
    for tag in find_all_in_table:
        previous_versions_column = []
        version_column = tag.find('td', {'class': 'versionColumn'}).text.strip()
        date_column = tag.find('td', {'class': 'dateColumn'}).text.strip()
        versions_column = tag.find('td', {'class': 'previousVersionsColumn'}).text.strip().split()
        for version_comma in versions_column:
            version_no_comma = version_comma.replace(",", "").strip()
            previous_versions_column.append(version_no_comma)

        min_versions_column = tag.find('td', {'class': 'previousVersionsColumn'}).text.strip()
        # Получить ссылки релиза
        response = requests_release_path.request(session,data_for_auth.format_link_download(version_column))
        data_list_download = parser_link_download(response)

        data[number] = {version_column: {
            "dateColumn": date_column,
            'previousVersionsColumn': previous_versions_column,
            'minVersionsColumn': min_versions_column,
            'links_release': data_list_download
        }}
        formatted_time = time.ctime(time.time())
        print(f"информация о релизе {version_column} собрана время {formatted_time}")
        if version_column == "3.0.40.2":
            break
        number += 1
    return data


def find_path(soup):
    data = {}
    number = 0
    find_all_in_table = soup.find('table', {'id': "versionsTable"}).find('tbody').find_all('tr')
    for tag in find_all_in_table:
        key_download = tag.find('input', {'class': 'download-flag'}).get('value')
        name_column = tag.find('td', {'class': 'nameColumn with-file-info-tooltip'}).text.strip()
        description_column = tag.find('div',
                                      {'class':
                                           'modal-body'}).find('pre',
                                                               {
                                                                   'class':
                                                                       'descriptionColumn'}).text.strip()
        date_column = tag.find('td', {'class': 'dateColumn'}).text.strip()

        data[number] = {name_column: {
            "key_download": key_download,
            "description_column": description_column,
            "date_column": date_column

        }}
        number += 1
    return data


def find_link(soup: BeautifulSoup):
    number = 0
    data_list = []
    find_all_in_table = soup.find('div', {'class': "downloadDist"}).find_all('a')

    for tag in find_all_in_table:
        download_link_release = tag['href']

        data_list.append(download_link_release)

        number += 1
    return data_list


def parser_path(address):
    html = write_read_html_json.read_out_html(address)
    soup = BeautifulSoup(html, 'lxml')
    data = find_path(soup)
    return data


def parser_release(session, response_html):
    # src = write_read_html_json.read_out_html(data_for_auth.LOCAL_ADDRESS_RELEASE_HTML)
    soup = BeautifulSoup(response_html, 'lxml')
    data = find_versions(session, soup)
    return data


def parser_link_download(response_html):
    soup = BeautifulSoup(response_html.text, 'lxml')
    data_list = find_link(soup)
    return data_list


def parser_hidden_auth(response_html):
    soup = BeautifulSoup(response_html.text, 'lxml')
    hidden_inputs = soup.find_all("input", type="hidden")
    data = {}
    for input_tag in hidden_inputs:
        data[input_tag.get("name")] = input_tag.get("value")


if __name__ == '__main__':
    # import data_for_auth
    current_time = time.time()
    formatted_time = time.ctime(current_time)
    print(formatted_time)
    # print(parser_path(data_for_auth.LOCAL_ADDRESS_PATH_HTML))
