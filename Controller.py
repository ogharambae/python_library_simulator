from store_front_controller import StoreFrontController
from order_processor import OrderProcessor
from ui_message import UIMessage


class Controller:
    def __init__(self):
        self.store_front_controller = StoreFrontController()
        filename = self.try_catch_filename()
        self.order_processor_controller = OrderProcessor(filename)

    def run(self):
        end_program = False
        while not end_program:
            user_input = self.try_catch_user_input()
            match user_input:
                case "1":
                    return self.check_inventory()
                case "2":
                    return self.store_front_controller
                case "3":
                    end_program = True
        print(UIMessage.exit_message())

    def check_inventory(self):
        for item in self.store_front_controller.store.inventory.item_stock:
            if item["quantity"] > 10:
                print(item["name"] + ": " + "In Stock")
            elif 10 > item["quantity"] > 3:
                print(item["name"] + ": " + "Low")
            elif 3 > item["quantity"] > 0:
                print(item["name"] + ": " + "Very Low")
            else:
                print(item["name"] + ": " + "Out of Stock")

    def process_web_orders(self, filename):
        pass

    @classmethod
    def try_catch_filename(cls):
        while True:
            try:
                filename = input("Please enter in the filename you wish to open: ")
                if filename.strip() == "":
                    raise ValueError
                elif not isinstance(filename, str):
                    raise ValueError
            except ValueError:
                print(UIMessage.invalid_file_name_message())
            else:
                return filename

    @classmethod
    def try_catch_user_input(cls):
        while True:
            try:
                user_input = input(UIMessage.display_ui_menu())
                if user_input not in ["1", "2", "3"]:
                    raise ValueError
            except ValueError:
                print(UIMessage.invalid_menu_input_message())
                continue
            else:
                return user_input
