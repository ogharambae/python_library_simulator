class Inventory:
    """
    Represent the Inventory class of the store which contains the item stock information
    """

    def __init__(self):
        self.item_stock = {}

    def check_stock(self, order):
        """
        Returns True if there is stock of the specified order.

        :return: True if there is stock of the specified order
        """
        item = order.item
        if item.get_inventory_key() in self.item_stock:
            if self.item_stock[item.get_inventory_key()] > order.get_quantity():
                return True
        else:
            self.item_stock[item.get_inventory_key()] = 0

    def restock(self, item):
        """
        Restocks an item by a count of 100.
        """
        self.item_stock[item.get_inventory_key()] += 100

    def fulfill_order(self, order):
        """
        Reduces the amount of stock of a specified item by the specified amount.
        """
        self.item_stock[order.item.get_inventory_key()] -= order.get_quantity()
