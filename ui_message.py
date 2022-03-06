class UIMessage:

    @staticmethod
    def print_error_message(error_message):
        print("Order %d, Could not process order data. %s" % error_message)

    @staticmethod
    def stuffed_animal_error():
        return "Color can only be White, Grey, Pink or Blue"
