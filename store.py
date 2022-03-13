from inventory import Inventory


class Store:
    """
    Represents the Store object of the program.
    """

    def __init__(self):
        self.inventory = Inventory()
        self.orders = []

    @property
    def orders(self):
        """
        Returns the list of orders stored in the Store.

        :return: a list representing a list of orders
        """
        return self._orders

    @orders.setter
    def orders(self, orders):
        """
        Sets the list of orders stored in the Store.
        """
        self._orders = orders

    def append_order(self, order):
        """
        Adds a new order to the list of orders stored in Store.
        """
        self.orders.append(order)

    def get_inventory_stock_list(self):
        """
        Return the inventory of this instance of Store.

        :return: inventory as a list
        """
        return self.inventory.item_stock
