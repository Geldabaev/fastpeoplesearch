import requests
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup


def criminal_info(name: str) -> list:
    name = str(name).encode("windows-1251")
    print(name, "***")
    url_en = {"D": name}
    n = urllib.parse.urlencode(url_en)
    url = f"https://fsin.gov.ru/criminal/?arrFilterAdd_pf%5Bterritory2%5D=&arrFilterAdd_pf%5Bfio%5{n}&set_filter=&set_filter=Y"
    session = requests.Session()
    r = session.get(url)
    # if r.status_code == 200:
    #     pass
        # with open("index.html", 'wb') as fb:
        #     for chunk in r.iter_content(chunk_size=128):
        #         fb.write(chunk)
    # else:
    #     print("Что-то пошло не так!")

    # with open("index.html", encoding="windows-1251") as fp:
    soup = BeautifulSoup(r.text, 'lxml')

    soup_res = soup.findAll("div", class_="sl-item")

    if len(soup_res) == 0:
        print(f"Ориентировки на {name} нет!")
        return ["Ориентировки на это имя нет!"]

    criminals = []
    for i in soup_res:
        print("*" * 50)
        title = i.div.img.get("title").strip()
        info = i.find("div", class_="sl-item-text").text.strip()
        criminals.append(title)
        criminals.append(info)
        criminals.append("*" * 50)
    return criminals
