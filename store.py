from Inventory import Inventory


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
        return self.orders

    @orders.setter
    def orders(self, orders):
        """
        Sets the list of orders stored in the Store.
        """
        self.orders = orders

    def append_order(self, order):
        """
        Adds a new order to the list of orders stored in Store.
        """
        self.orders.append(order)
