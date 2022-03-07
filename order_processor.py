from order import Order
from factory_mapping import FactoryMapping
from file_manager import FileManager


class OrderProcessor:
    """
    Represent the Order Processor to process the data received from File Manager and instantiates orders
    """

    def __init__(self, filename):
        """
        Instantiate an object to process the order
        """
        self._data = self.import_data(filename)

    @classmethod
    def import_data(cls, filename):
        """
        Import the data from the FileManager class.

        :return: data containing the order information
        """
        data = FileManager.read_file(filename)
        return data

    def get_data(self):
        """
        Return the data.
        :return: data
        """
        return self._data

    def create_order(self) -> list:
        """
        Create Order objects with information through data.
        :return: the list of Order objects
        """
        data = self.get_data()
        order_list = []

        for order_data in data:
            item = order_data['item']
            holiday = order_data["holiday"]
            order_data["item_factory"] = FactoryMapping.get_item_factory(holiday, item)
            new_order = Order(**order_data)
            order_list.append(new_order)

        return order_list


# def main():
#     filename = "./orders.xlsx"
#     my_order = OrderProcessor(filename)
#     order_list = my_order.create_order()
#     FileManager.write_report(order_list)
#
#
# if __name__ == '__main__':
#     main()

