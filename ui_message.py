class UIMessage:

    @staticmethod
    def print_error_message(error_message):
        print("Order %d, Could not process order data. %s" % error_message)

    @staticmethod
    def stuffed_animal_error():
        return "Color can only be White, Grey, Pink or Blue"

    @staticmethod
    def toffee_error_message():
        return "Color can only be White, Grey, Pink or Blue"

    @staticmethod
    def candy_cane_error_message():
        return "Stripes must be either Red or Green"

    @staticmethod
    def creme_eggs_error_message():
        return "Packet size must be greater than Zero"

    @staticmethod
    def spider_type_error_message():
        return "RC Spider Type must be either Tarantula or Wolf"

    @staticmethod
    def robot_bunny_colour_error_message():
        return "Bunny Colour must be either Orange, Blue or Pink"

    @staticmethod
    def stuffing_type_error_message():
        return "Stuffing must be either Polyester FiberFill or Wool"

    @staticmethod
    def size_error_message():
        return "Size must be either small, medium or large"

    @staticmethod
    def fabric_error_message():
        return "Fabric type must be either Linen, Cotton or Acrylic"

    @staticmethod
    def order_type_message():
        return "Item Type Must be either Toy, Candy or Stuffed Animal"

    @staticmethod
    def invalid_file_name_message():
        return "The file name you have entered is an invalid file name."

    @staticmethod
    def display_ui_menu():
        return f"Please select from one of the following 3 options: \n" \
               f"1. Process Web Orders\n" \
               f"2. Check Inventory\n" \
               f"3. Exit\n"

    @staticmethod
    def invalid_menu_input_message():
        return "Invalid input. Please enter in either 1, 2 or 3."

    @staticmethod
    def exit_message():
        return "Printing out and exiting the program."

    @staticmethod
    def file_not_found_message():
        return "Error: Cannot find the file."

    @staticmethod
    def file_invalid_excel_message():
        return "Error: Unsupported file type, accept excel file xlsx only."

    @staticmethod
    def web_order_processed_successfully():
        return "Success! System successfully processed your web orders"
