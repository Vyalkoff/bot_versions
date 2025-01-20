import requests_release_path
import json


def update_file_html_path(message_path):
    requests_release_path.request_path(message_path)




if __name__ =='__main__':
    update_file_html_path("3.0.60.1")