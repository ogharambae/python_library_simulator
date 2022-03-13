from store import Store
from file_manager import FileManager


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
                self.store.append_order(order)
                return

            if self.store.inventory.check_stock(order):
                self.store.inventory.fulfill_order(order)
                self.store.append_order(order)
            else:
                self.store.inventory.restock(order.item)
                self.store.inventory.fulfill_order(order)
                self.store.append_order(order)
        return self.store.orders

    def get_imported_orders(self):
        """
        Returns the imported list of orders from the Store.

        :return: a list representing a list of orders
        """
        return self.store.orders

    def generate_daily_transaction_report(self):
        """
        Generate daily transaction report for all orders stored in instance variable Store.
        """
        FileManager.write_report(self.store.orders)

    def get_store_inventory(self):
        """
        Return the inventory of the store in this instance of store from controller.

        :return: inventory as a list
        """
        return self.store.get_inventory_stock_list()

    def check_inventory(self):
        """
        Check inventory and print total stock levels.
        """
        if len(self.get_store_inventory()) == 0:
            print("Currently, there is no items in the inventory!")
            return

        for inventory_key, item in self.get_store_inventory().items():
            if item["quantity"] >= 10:
                print(item["name"].title() + ": Total qty -> " + str(item["quantity"]) + ", In Stock")
            elif 10 > item["quantity"] >= 3:
                print(item["name"].title() + ": Total qty -> " + str(item["quantity"]) + ", Low")
            elif 3 > item["quantity"] > 0:
                print(item["name"].title() + ": Total qty -> " + str(item["quantity"]) + ", Very Low")
            else:
                print(item["name"].title() + ": Total qty -> " + str(item["quantity"]) + ", Out of Stock")
