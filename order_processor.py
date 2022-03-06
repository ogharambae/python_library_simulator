from Order import Order
from file_manager import FileManager


class OrderProcessor:
    """
    Represent the Order Processor to process the data received from File Manager and instantiates orders
    """

    def __init__(self, filename):
        self._data = self.import_data(filename)

    @classmethod
    def import_data(cls, filename):
        data = FileManager.write_report(filename)
        return data

    def get_data(self):
        return self._data

    def create_order(self):
        data = self.get_data()
        order_list = []

        for order_data in data:
            new_order = Order(order_data)
            order_list.append(new_order)
        return order_list




