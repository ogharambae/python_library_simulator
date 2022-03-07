from Store import Store


class StoreFrontController:
    """
    Represents the Store Front Controller of the program.
    """
    def __init__(self):
        self.store = Store()

    def import_order(self, orders):
        """
        Returns a list of updated orders.

        :return: a list representing an updated list of orders
        """
        for order in orders:
            if not order.order_success:
                continue
            if self.store.inventory.check_stock(order):
                self.store.inventory.fulfill_order(order)
                self.store.append_order(order)
            else:
                self.store.inventory.restock()
                self.store.inventory.fulfill_order(order)
                self.store.append_order(order)
        return self.store.orders

    def get_imported_orders(self):
        """
        Returns the imported list of orders from the Store.

        :return: a list representing a list of orders
        """
        return self.store.orders
