import requests
import os
import bz2, shutil


__all__ = ['ScheduleDownloadFile']

url_pasport = "https://проверки.гувм.мвд.рф/upload/expired-passports/list_of_expired_passports.csv.bz2"


class ScheduleDownloadFile():
    def __init__(self, url: str = url_pasport, name_folder: str = 'db_files'):
        self.url: str = url
        self.name_folder: str = name_folder
        self.download_file()  # <<<<<<<<<<<<<<<<<<<<
        self.name_arhive: str = self.read_in_folder()
        self.extract_here()
        self.remove_arhive()  # <<<<<<<<<<<<<<<<<<<<

    def download_file(self):
        '''Скачать файл'''
        print("[*] Скачивается база данных...")
        r = requests.get(self.url, allow_redirects=True)
        open('flask_app/models/schedule_download/db_files/pasports.bz2', 'wb').write(r.content)

    def read_in_folder(self) -> str:
        """Прочесть название архива из папки"""
        print("[*] Проверяем файл...")
        for filename in os.listdir(f'flask_app/models/schedule_download/{self.name_folder}'):
            bz = filename.endswith("bz2")
            if bz:
                return filename.strip()

    def extract_here(self):
        """Рспаковка файла"""
        print("[*] Распаковка файла...")


        filepath = f"flask_app/models/schedule_download/db_files/{self.name_arhive}"
        with bz2.BZ2File(filepath) as fr, open(filepath[:-4], "wb") as fw:
            shutil.copyfileobj(fr, fw)

        # ifile.close()
        print("Успешно распаковано!")

    def remove_arhive(self):
        print("[*] Удаление архива для экономия памяти...")
        # удаление архива после извлечения из него файла
        os.remove(f"flask_app/models/schedule_download/db_files/{self.name_arhive}")
        print("ГОТОВО!")


# ScheduleDownloadFile(url_pasport, "db_files")

