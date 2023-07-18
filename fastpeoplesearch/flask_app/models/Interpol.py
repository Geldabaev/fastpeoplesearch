import requests
import json
from pprint import pprint


def interpol_mod(name: str, forename: str) -> list:
    payload = {
        "name": name,
        "forename": forename
    }

    url ="https://ws-public.interpol.int/notices/v1/red?"

    file = requests.get(url, params=payload).json()
    # data = n.json()
    # with open("interpol.json", 'w') as f:
    #     json.dump(data, f)

    # print(n.url)

    # with open("interpol.json", 'r') as f:
    #     file = json.load(f)

    # if file['total'] == 1:
    if file['total'] == 1:
        print('ЧИСЛИТСЯ В ИНТЕРПОЛЕ!')
        print(f"Имя: {file['query']['name']}")
        print(f"Фамилия: {file['query']['forename']}")
        print(f"Дата рождения: {file['_embedded']['notices'][0]['date_of_birth']}")
        print(f"Национальность: {file['_embedded']['notices'][0]['nationalities'][0]}")
        return ["ЧИСЛИТСЯ В ИНТЕРПОЛЕ!", f"Имя: {file['query']['name']}", f"Фамилия: {file['query']['forename']}",
                f"Дата рождения: {file['_embedded']['notices'][0]['date_of_birth']}",
                f"Национальность: {file['_embedded']['notices'][0]['nationalities'][0]}"]
    else:
        print("НЕ ЧИСЛИТСЯ В ИНТЕРПОЛЕ!")
        return ["НЕ ЧИСЛИТСЯ В ИНТЕРПОЛЕ!"]


# res = interpol()
