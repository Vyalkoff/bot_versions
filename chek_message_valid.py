import json
import re


def valid(message_text):
    # pattern = re.compile(r'')
    text = message_text.strip()
    with open("data_release_json/release.json", encoding="utf-8") as file:
        data = json.load(file)
        len_data = len(data) - 1

        for number in range(len_data):
            for key in data[str(number)].keys():
                if key == text:
                    return True





if __name__ == '__main__':
    valid("3.0.50.1")
