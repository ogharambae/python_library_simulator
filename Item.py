from abc import ABC


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


class Toys(ABC, Item):
    """
    An abstract class which extends Item and represents a Toy
    """

    def __init__(self, name: str, description: str,
                 product_id: str, has_battery: bool, min_age: int):
        """
        Initialize this instance of Toy.

        :param name: a string
        :param description: a string
        :param product_id: a string
        :param has_battery: a boolean
        :param min_age: an int
        """

        super().__init__(name, description, product_id)
        self._has_battery = has_battery
        self._min_age = min_age

    def get_battery(self):
        """
        Return the battery status of this Toy,
        True if Toy has battery, else False.

        :return: a boolean representing battery status
        """
        return self._has_battery

    def get_min_age(self):
        """
        Return the minimum recommend age for this Toy.

        :return: an integer representing the minimum age
        """
        return self._min_age


class StuffedAnimals(ABC, Item):
    """
    An abstract class which extends Item and represents a Stuffed Animal.
    """

    # we may want to change stuffing, size and fabric to be an enum,
    # as options for stuffing (poly, fiberfill, wool), size (small, medium, large),
    # and fabric (linen, cotton or acrylic) are all limited!

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
        self._stuffing_type = stuffing
        self._size = size
        self._fabric = fabric

    def get_stuffing_type(self):
        """
        Return the stuffing type for this instance of Stuffed Animal.

        :return: a string representing stuffing type
        """
        return self._stuffing_type

    def get_size(self):
        """
        Return the size of this instance of Stuffed Animal.

        :return: a string representing size
        """
        return self._size

    def get_fabric(self):
        """
        Return the fabric of this instance of Stuffed Animal.

        :return: a string representing fabric type
        """
        return self._fabric


class Candy(ABC, Item):
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
