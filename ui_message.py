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
    def robot_bunny_color_error_message():
        return "Bunny Color must be either Orange, Blue or Pink"

    @staticmethod
    def stuffing_type_error_message():
        return "Stuffing must be either Polyester FiberFill or Wool"

    @staticmethod
    def size_error_message():
        return "Size must be either small, medium or large"

    @staticmethod
    def fabric_error_message():
        return "Fabric type must be either Linen, Cotton or Acrylic"
