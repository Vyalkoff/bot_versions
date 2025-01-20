import json
import write_read_html_json
from bs4 import BeautifulSoup
import data_for_auth


# def create_dict(**qwargs):
#     d = {k: v for k, v in qwargs.items()}
#     return d


# table = soup.find('table', {'id': "versionsTable"}).find('tbody').find_all('tr')


def find_versions(soup):
    number = 0
    data = {}
    # if number ==1:
    #     find_all_in_table = soup.find('table', {'id': "versionsTable"}).find('tbody').find_all('tr')[0]
    # else:
    find_all_in_table = soup.find('table', {'id': "versionsTable"}).find('tbody').find_all('tr')

    for tag in find_all_in_table:
        previous_versions_column = []
        version_column = tag.find('td', {'class': 'versionColumn'}).text.strip()
        date_column = tag.find('td', {'class': 'dateColumn'}).text.strip()
        versions_column = tag.find('td', {'class': 'previousVersionsColumn'}).text.strip().split()
        for version_comma in versions_column:
            version_no_comma = version_comma.replace(",", "").strip()
            previous_versions_column.append(version_no_comma)

        min_versions_column = tag.find('td', {'class': 'previousVersionsColumn'}).text.strip()
        data[number] = {version_column: {
            "dateColumn": date_column,
            'previousVersionsColumn': previous_versions_column,
            'minVersionsColumn': min_versions_column
        }}
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

 
def parser_path(address):
    html = write_read_html_json.read_out_html(address)
    soup = BeautifulSoup(html, 'lxml')
    data = find_path(soup)
    return data


def parser_release():
    src = write_read_html_json.read_out_html(data_for_auth.LOCAL_ADDRESS_RELEASE_HTML)
    soup = BeautifulSoup(src, 'lxml')
    data = find_versions(soup)
    return data


if __name__ == '__main__':
    import data_for_auth

    print(parser_path(data_for_auth.LOCAL_ADDRESS_PATH_HTML))
