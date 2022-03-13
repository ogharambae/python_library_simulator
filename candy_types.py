from item import Candy
from item_enum import ToffeeVariety, CandyCaneVariety
from invalid_data_error import InvalidDataError
from ui_message import UIMessage


class PumpkinCaramelToffee(Candy):
    """
    Represent a piece of Pumpkin Caramel Toffee, extending abstract
    class of Candy.
    """

    def __init__(self, name: str, description: str,
                 product_id: str, variety, has_nuts=True, has_lactose=True, **kwargs):
        """
        Initialize this instance of Pumpkin Caramel Toffee.

        :param name: a string
        :param description: a string
        :param product_id: a string
        :param has_nuts: a boolean True by default
        :param has_lactose: a boolean True by default
        :param variety: a string, either a Sea Salt or Regular
        """

        super().__init__(name, description, product_id, has_nuts, has_lactose)
        self.variety = variety
        self.inventory_key = "pct_" + str(variety)

    @property
    def variety(self):
        """
        Return the variety of this Pumpkin Caramel Toffee.

        :return: a string representing variety of Pumpkin Caramel Toffee
        """
        return self._variety

    @variety.setter
    def variety(self, variety_type: str):
        """
        Set the variety of this instance of Pumpkin Caramel Toffee.

        :param variety_type: string
        :precondition variety_type: variety type must be either "Sea Salt" or "Regular"
        """

        if variety_type.lower() not in [e.value for e in ToffeeVariety]:
            raise InvalidDataError(UIMessage.toffee_error_message())

        self._variety = variety_type

    def __str__(self):
        """
        Generate a string representation of this instance of Pumpkin Caramel Toffee.

        :return: a string representing this instance of Pumpkin Caramel Toffee
        """

        return "Item Candy, Product ID: {}, Name: {}, May Contain Nuts," \
               " Contains Lactose, Variety: {}".format(self.get_product_id(),
                                                       self.get_name(), self.variety)


class CandyCane(Candy):
    """
    Represent a Candy Cane, which extends the abstract class of Candy.
    """

    def __init__(self, name: str, description: str,
                 product_id: str, colour: str, has_nuts=False, has_lactose=False, **kwargs):
        """
        Initialize this instance of CandyCane.

        :param name: a string
        :param description: a string
        :param product_id: a string
        :param colour: a string, either "Red" or "Green"
        :param has_nuts: A boolean False by default
        :param has_lactose: a boolean False by default
        """
        super().__init__(name, description, product_id, has_nuts, has_lactose)
        self.colour = colour
        self.inventory_key = "cc_" + str(colour)

    @property
    def colour(self):
        """
        Return the stripe color of this instance of CandyCane.

        :return: a string, either "Red" or "Green"
        """
        return self._colour

    @colour.setter
    def colour(self, colour):
        """
        Set the stipe type of this instance of Candy Cane.

        :param colour: a string
        :precondition: must be either "Red" or "Green"
        """
        if colour.lower() not in [e.value for e in CandyCaneVariety]:
            raise InvalidDataError(UIMessage.candy_cane_error_message())

        self._colour = colour

    def __str__(self):
        """
        Generate a string representation of this instance of CandyCane.

        :return: a string representing this instance of Candy Cane
        """

        return "Item Candy, Product ID: {}, Name: {}, Does Not Contain Nuts," \
               " Does Not Contain Lactose, Stripes: {}".format(self.get_product_id(),
                                                               self.get_name(), self.colour)


class CremeEgg(Candy):
    """
    Represent a CremeEgg, which extends the abstract class of Candy.
    """

    def __init__(self, name: str, description: str,
                 product_id: str, pack_size: int, has_nuts=True, has_lactose=True, **kwargs):
        """
        Initialize this instance of CremeEgg.

        :param name: a string
        :param description: a string
        :param product_id: a string
        :param pack_size: an int representing number of eggs in pack
        :param has_nuts: boolean true by default
        :param has_lactose: boolean true by default
        """

        super().__init__(name, description, product_id, has_nuts, has_lactose)
        self.pack_size = pack_size
        self.inventory_key = "ce_" + str(pack_size)

    @property
    def pack_size(self):
        """
        Return the pack size of this instance of CremeEgg.

        :return: an int representing the pack size of CremeEgg
        """
        return self._pack_size

    @pack_size.setter
    def pack_size(self, num_eggs: int):
        """
        Set the pack size of this instance of Candy Cane.

        :param num_eggs: an int
        :precondition num_eggs: must be an int value greater than zero
        """
        if num_eggs < 0:
            raise InvalidDataError(UIMessage.creme_eggs_error_message())

        self._pack_size = num_eggs

    def __str__(self):
        """
        Generate a string representation of this instance of CremeEgg.

        :return: a string representing this instance of Candy Cane
        """

        return "Item Candy, Product ID: {}, Name: {}, Contain Nuts," \
               "Contains Lactose, Pack Size: {}".format(self.get_product_id(),
                                                        self.get_name(), self.pack_size)
