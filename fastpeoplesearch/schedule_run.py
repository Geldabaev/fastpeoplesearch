import schedule
import time
from flask_app.models import ScheduleDownloadFile
from flask_app.models import save_and_xlsx_to_sqlite3


schedule.every().day.at("00:00").do(ScheduleDownloadFile)
schedule.every().day.at("03:00").do(save_and_xlsx_to_sqlite3)


def main():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
