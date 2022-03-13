from datetime import datetime
from pathlib import Path

import pandas as pd
from order import Order
from ui_message import UIMessage


class FileManager:
    """
    Represent the File Manager which involves in file io operations
    """

    @staticmethod
    def read_file(filename) -> list:
        """
        Read Excel file and process data to list of dictionary.
        """

        list_of_order = []

        if Path(filename).is_file():
            df = pd.read_excel(filename)
            df = df.fillna('')
            df = df.applymap(lambda s: s.lower() if type(s) == str else s)
            df = df.applymap(
                lambda s: True if s == "y" else (False if s == "n" else s) if type(s) == str else s).to_dict('records')
            for column in df:
                list_of_order.append(column)
        else:
            raise FileNotFoundError
        return list_of_order

    @staticmethod
    def write_report(orders: list[Order]):
        """
        Write the daily transaction report into a text file.
        """
        processing_time = datetime.now()
        date = processing_time.strftime("%d%m%y")
        time = processing_time.strftime("%H%M")

        doc_name = 'DTR_' + date + "_" + time + ".txt"

        daily_transactions = orders

        with open(doc_name, 'w') as f:
            f.write('HOLIDAY STORE - DAILY TRANSACTION REPORT (DRT) \n' +
                    processing_time.strftime("%d-%m-%Y %H:%M") + '\n')

        for transaction in daily_transactions:
            with open(doc_name, 'a') as f:
                f.write(transaction.__str__() + '\n')
