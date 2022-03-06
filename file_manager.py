import pandas as pd


class FileManager:
    """
    Represent the File Manager which involves in file io operations
    """

    @staticmethod
    def write_report():
        """
        Read Excel file and process data to list of dictionary.
        """

        list_of_order = []

        df = pd.read_excel(r"./orders.xlsx", index_col=0, na_values=['NA']).to_dict('records')

        for column in df:
            list_of_order.append(column)

        return list_of_order


def main():
    FileManager.write_report()


if __name__ == '__main__':
    main()

