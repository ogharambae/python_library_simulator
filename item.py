from abc import ABC
from invalid_data_error import InvalidDataError
from item_enum import StuffingType, FabricType, SizeOptions
from ui_message import UIMessage


class Item(ABC):
    """
    An abstract class representing an inventory item with a name,
    description and product ID.
    """

    def __init__(self, name: str, description: str, product_id: str):
        """
        Initialize an Item with a name, description and product id.

        :param name: a string
        :param description: a string
        :param product_id: a string
        """
        self._name = name
        self._description = description
        self._product_ID = product_id
        self.inventory_key = None

    def get_name(self):
        """
        Return the name of this instance of Item.

        :return: a string representing a name
        """
        return self._name

    def get_description(self):
        """
        Return the description of this item.

        :return: a string representing a description
        """
        return self._description

    def get_product_id(self):
        """
        Return the product ID of this item.

        :return: a string representing product id
        """
        return self._product_ID

    def get_inventory_key(self):
        return self.inventory_key


class Toys(Item, ABC):
    """
    An abstract class which extends Item and represents a Toy
    """

    def __init__(self, name: str, description: str,
                 product_id: str, has_batteries: bool, min_age: int):
        """
        Initialize this instance of Toy.

        :param name: a string
        :param description: a string
        :param product_id: a string
        :param has_batteries: a boolean
        :param min_age: an int
        """

        super().__init__(name, description, product_id)
        self._has_batteries = has_batteries
        self._min_age = min_age

    def get_battery(self):
        """
        Return the battery status of this Toy,
        True if Toy has battery, else False.

        :return: a boolean representing battery status
        """
        return self._has_batteries

    def get_min_age(self):
        """
        Return the minimum recommend age for this Toy.

        :return: an integer representing the minimum age
        """
        return self._min_age


class StuffedAnimals(Item, ABC):
    """
    An abstract class which extends Item and represents a Stuffed Animal.
    """

    def __init__(self, name: str, description: str,
                 product_id: str, stuffing: str, size: str, fabric: str):
        """
        Initialize this instance of Stuffed Animal.

        :param name: a string
        :param description: a string
        :param product_id: a string
        :param stuffing: a string
        :param size: a string
        :param fabric: a string
        """

        super().__init__(name, description, product_id)
        self.stuffing_type = stuffing
        self.size = size
        self.fabric = fabric

    @property
    def stuffing_type(self):
        """
        Return the stuffing type for this instance of Stuffed Animal.

        :return: a string representing stuffing type
        """
        return self._stuffing_type

    @stuffing_type.setter
    def stuffing_type(self, stuffing: str):
        """
        Set the stuffing type for this instance of Stuffed Animal.

        :param stuffing: a string
        :precondition stuffing: must be either "Polyester FiberFill" or "Wool"
        """

        if stuffing not in [e.value for e in StuffingType]:
            raise InvalidDataError(UIMessage.stuffing_type_error_message())

        self._stuffing_type = stuffing

    @property
    def size(self):
        """
        Return the size of this instance of Stuffed Animal.

        :return: a string representing size
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Set the size for this instance of Stuffed Animal.

        :param size: a string
        :precondition size: must be either "small", "medium", or "large"
        """
        if size not in [e.value for e in SizeOptions]:
            raise InvalidDataError(UIMessage.size_error_message())

        self._size = size

    @property
    def fabric(self):
        """
        Return the fabric of this instance of Stuffed Animal.

        :return: a string representing fabric type
        """
        return self._fabric

    @fabric.setter
    def fabric(self, fabric_type):
        """
        Set the fabric type of this instance of Stuffed Animal.

        :param fabric_type: a string
        :precondition fabric_type: must be either "Linen", "Cotton", or "Acrylic"
        """
        if fabric_type not in [e.value for e in FabricType]:
            raise InvalidDataError(UIMessage.fabric_error_message())
        self._fabric = fabric_type


class Candy(Item, ABC):
    """
    An abstract class which extends Item and represents Candy.
    """

    def __init__(self, name: str, description: str,
                 product_id: str, has_nuts: bool, has_lactose: bool):
        """
        Initialize this instance of Candy.

        :param name: a string
        :param description: a string
        :param product_id: a string
        :param has_nuts: a boolean
        :param has_lactose: a boolean
        """

        super().__init__(name, description, product_id)
        self._has_nuts = has_nuts
        self._has_lactose = has_lactose

    def get_nuts(self):
        """
        Return whether this candy object has nuts.

        :return: boolean representing whether candy has nuts
        """
        return self._has_nuts

    def get_lactose(self):
        """
        Return whether this candy object has lactose.

        :return: boolean representing whether candy has lactose
        """
        return self._has_lactose
