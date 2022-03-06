import pandas as pd


class FileManager:
    """
    Represent the File Manager which involves in file io operations
    """

    # def __init__(self, filename):
    #     self._file_manager = self.write_report(filename)

    @classmethod
    def read_file(cls, filename) -> list:
        """
        Read Excel file and process data to list of dictionary.
        """

        list_of_order = []

        df = pd.read_excel(filename, index_col=0)
        df = df.applymap(lambda s: s.lower() if type(s) == str else s).to_dict('records')

        for column in df:
            list_of_order.append(column)
        return list_of_order


# def main():
#     filename = "./orders.xlsx"
#     FileManager.write_report(filename)
#
#
# if __name__ == '__main__':
#     main()

