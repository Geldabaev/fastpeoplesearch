import requests
from enum import Enum


class DocumentType(Enum):
    # Паспорт гражданина СССР
    passport_ussr = "01"
    # Свидетельство о рождении
    birth_certificate = "03"
    # Паспорт иностранного гражданина
    passport_foreign = "10"
    # Вид на жительство в России
    residence_permit = "12"
    # Разрешение на временное проживание в России
    residence_permit_temp = "15"
    # Свидетельство о предоставлении временного убежища на территории России
    asylum_certificate_temp = "19"
    # Паспорт гражданина России
    passport_russia = "21"
    # Свидетельство о рождении, выданное уполномоченным органом иностранного государства
    birth_certificate_foreign = "23"
    # Вид на жительство иностранного гражданина
    residence_permit_foreign = "62"

class InnInfo():
    def suggest_inn(surname, name, patronymic, birthdate, doctype, docnumber, docdate):
        url = "https://service.nalog.ru/inn-proc.do"
        data = {
            "fam": surname,
            "nam": name,
            "otch": patronymic,
            "bdate": birthdate,
            "bplace": "",
            "doctype": doctype,
            "docno": docnumber,
            "docdt": docdate,
            "c": "innMy",
            "captcha": "",
            "captchaToken": "",
        }
        resp = requests.post(url=url, data=data)
        resp.raise_for_status()
        return resp.json()

    def main(self, last, first, surname, date, docnumber, docdate):
        response = InnInfo.suggest_inn(
            surname=last,
            name=first,
            patronymic=surname,
            birthdate=date,
            doctype=DocumentType.passport_russia.value,
            docnumber=docnumber,
            docdate=docdate,
        )
        print(response)
        return response


class Correction():
    @classmethod
    def correct_date(cls, date):
        date = date.replace('-', '.').split('.')
        d = date[-1]
        m = date[-2]
        y = date[0]
        date = [d, m, y]
        date = ".".join(date)
        print(date)
        return date

    @classmethod
    def correct_docnumber(cls, docnumber):
        a = docnumber[:2]
        b = docnumber[2:4]
        c = docnumber[4:]
        return a + " " + b + " " + c


def get_inn_info():
    return InnInfo()

