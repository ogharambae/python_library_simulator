from file_manager import FileManager


class OrderProcessor:
    """
    Represent the Order Processor to process the data received from File Manager and instantiates orders
    """

    def __init__(self, filename):
        self._data = FileManager(filename)


    def get_data(self):
        return self._data

    def create_order(self):



