from store_front_controller import StoreFrontController
from order_processor import OrderProcessor
from ui_message import UIMessage


class Controller:
    """
    Control flow of command for inventory system.
    """
    def __init__(self):
        """
        Initialize an instance of Controller.
        """
        self.store_front_controller = StoreFrontController()

    def run(self):
        """
        Run main menu of program.
        """
        end_program = False
        while not end_program:
            user_input = self.try_catch_user_input()
            match user_input:
                case "1":
                    self.process_web_orders()
                case "2":
                    self.check_inventory()
                case "3":
                    end_program = True
        self.store_front_controller.generate_daily_transaction_report()
        print(UIMessage.exit_message())

    def check_inventory(self):
        """
        Check current inventory levels in current instance of Store Front.
        """
        self.store_front_controller.check_inventory()

    def process_web_orders(self):
        """
        Process user-provided file, adding all order elements to store_front_controller.
        """
        filename = self.try_catch_filename()
        order_processor_controller = OrderProcessor(filename)
        order_list = order_processor_controller.create_order()
        self.store_front_controller.import_order(order_list)

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
