class Inventory:
    """
    Represent the Inventory class of the store which contains the item stock information
    """

    def __init__(self):
        """
        Initialize Inventory
        """
        self.item_stock = {}

    def check_stock(self, order):
        """
        Returns True if there is stock of the specified order.

        :return: True if there is stock of the specified order
        """
        item = order.item
        if item.get_inventory_key() in self.item_stock:
            if self.item_stock[item.get_inventory_key()]["quantity"] > order.get_quantity():
                return True
        else:
            data = {"quantity": 0, "name": item.get_name()}
            self.item_stock[item.get_inventory_key()] = data

    def restock(self, item):
        """
        Restocks an item by a count of 100.
        """
        self.item_stock[item.get_inventory_key()]["quantity"] += 100

    def fulfill_order(self, order):
        """
        Reduces the amount of stock of a specified item by the specified amount.
        """
        self.item_stock[order.item.get_inventory_key()]["quantity"] -= order.get_quantity()
