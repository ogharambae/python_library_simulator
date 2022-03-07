import pandas as pd
from order import Order
import math

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

        df = pd.read_excel(filename)
        df = df.fillna('')
        df = df.applymap(lambda s: s.lower() if type(s) == str else s).to_dict('records')

        for column in df:
            list_of_order.append(column)
        return list_of_order

    @staticmethod
    def write_report(orders: list[Order]):
        """
        Write the daily report into an excel file
        """
        pass


# def main():
#     filename = "./orders.xlsx"
#     data = FileManager.read_file(filename)
#     print("")
#
#
# if __name__ == '__main__':
#     main()
