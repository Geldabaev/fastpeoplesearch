import pandas as pd


class Analise():
    def __init__(self):
        self.df = pd.read_csv("flask_app/models/schedule_download/db_files/data_pasport.csv")
        print("Распаковка БД")
        self.file_extraction()

    def file_extraction(self):
        print("Анализ данных...")
        self.df['PASSP_SERIES'] = pd.to_numeric(self.df['PASSP_SERIES'], errors="coerce")
        self.df['PASSP_NUMBER'] = pd.to_numeric(self.df['PASSP_NUMBER'], errors="coerce")
        self.df = self.df.dropna()  # удаляем NaN

    def filter_data(self, series, number):
        series = int(series)
        number = int(number)
        print("Поиск...")
        res_filter = self.df[
            (self.df['PASSP_SERIES'] == series) &
            (self.df['PASSP_NUMBER'] == number)
            ]
        try:
            if len(res_filter['PASSP_NUMBER']) > 0:
                return """Паспорт найден среди списков недействительных (утраченных (похищенных),
                      оформленных на утраченных (похищенных) бланках паспорта гражданина Российской Федерации,
                      выданных в нарушение установленного порядка, а также признанных недействительными)"""
        except KeyError:
            print("Паспорт не найден в базе данных")
            return "Паспорт не найден в базе данных"


# Analise().filter_data(4621, 501925)
# test.filter_data(4621, 501925)
