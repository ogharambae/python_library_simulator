from invalid_data_error import InvalidDataError


class Order:
    """
    Represent the Order object which contains the detail of an order
    """

    def __init__(self, **kwargs):
        """
        Instantiate an object of type order

        :param order_num: an int
        :param product_id: a string
        :param item_type: a string
        :param item_name: a string
        :param product_detail: a string
        :param item: an item constructed within order
        """
        self._order_num = kwargs["order_number"]
        self._id = kwargs["product_id"]
        self._item_type = kwargs["item"]
        self._item_name = kwargs["name"]
        self._product_detail = kwargs
        self._item_factory = kwargs["item_factory"]
        self._order_success = None
        self._warning_message = ""
        self.item = kwargs

    @property
    def order_success(self):
        return self._order_success

    @property
    def item(self):
        """
        Return the item of this order.

        :return: a string representing item_type
        """
        return self._item

    @item.setter
    def item(self, item_info):
        """
        Instantiate an item based on Information in order.

        :param item_info: kwargs needed to construct item
        """

        try:
            new_inventory_item = self._item_factory(**item_info)
        except InvalidDataError as e:

            self._order_success = False
            self._warning_message = ("InvalidDataError " + e.message).format(self._order_num)
            self._item = None

        else:
            self._order_success = True
            self._item = new_inventory_item
            self._warning_message = None

    def get_order_num(self):
        """
        Return order number of this instance of order.

        :return: an int representing order number
        """
        return self._order_num

    def get_id(self):
        """
        Return id number of item in this instance order.

        :return: a string
        """
        return self._id

    def get_item_type(self):
        """
        Return item type for item in this instance of order.

        :return: a string
        """
        return self._item_type

    def get_item_name(self):
        """
        Return the item name for the item in this instance of order.

        :return: a string
        """
        return self._item_name

    def get_order_successful(self):
        """
        Return whether the order was successfully processed.

        :return: a boolean
        """
        return self._order_success

    def get_warning_message(self):
        """
        Return warning message for this order, used if Item could not be
        correctly constructed.

        :return: a string
        """
        return self._warning_message

    def get_quantity(self):
        """
        Returns the quantity amount within the product details of the item.
        """
        return self._product_detail["quantity"]

    def __repr__(self):
        return "Order [%d, %s, %s, %s]" % (
            self._order_num, self._item_name, self._item_type, "success" if self._order_success else "failed")

    def __str__(self):
        if self._order_success:
            return f'Order {self._order_num}, Item {self._item_type.title()}, Product ID {self.get_id().title()}, ' \
                   f'Name "{self._item_name.title()}", Quantity {self.get_quantity()}'
        else:
            return f'Order {self._order_num}, Could not process order data was corrupted, {self._warning_message}'
