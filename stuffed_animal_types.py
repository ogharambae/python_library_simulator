from item import StuffedAnimals
from item_enum import StuffingType, FabricType, EasterBunnyColours
from invalid_data_error import InvalidDataError
from ui_message import UIMessage


class DancingSkeleton(StuffedAnimals):
    """
    Represent a dancing skeleton, which extends the abstract class of
    StuffedAnimals
    """

    # Unsure if Dancing Skeleton glows in the dark by default!
    def __init__(self, name: str, description: str,
                 product_id: str, size: str, has_glow: bool,
                 stuffing=StuffingType.POLY.value, fabric=FabricType.ACRYLIC.value, **kwargs):
        """
        Initialize this instance of Dancing Skeleton.

        :param name: a string
        :param description: a string
        :param product_id: a string
        :param size: a string
        :param has_glow: a boolean, true if Glows in dark
        :param stuffing: a string
        :param fabric: a string
        """

        super().__init__(name, description, product_id, stuffing, size, fabric)
        self._has_glow = has_glow
        self.inventory_key = "ds"

    def get_glows_in_dark(self):
        """
        Return whether this Dancing Skeleton glows in dark.

        :return: a boolean
        """
        return self._has_glow

    def __str__(self):
        """
        Generate a string representation of this instance of Dancing Skeleton.

        :return: a string representation of DancingSkeleton
        """
        return "Item StuffedAnimal, Product ID: {}, Name: {}, Glows in Dark {}," \
               " Size {}, Stuffing: {}, Fabric: {}".format(self.get_product_id(),
                                                           self.get_name(), self.get_glows_in_dark(),
                                                           self.size, self.stuffing_type, self.fabric)


class Reindeer(StuffedAnimals):
    """
    Represent a Reindeer which extends the abstract class StuffedAnimals.
    """

    def __init__(self, name: str, description: str,
                 product_id: str, size: str, has_glow: bool,
                 stuffing=StuffingType.WOOL.value, fabric=FabricType.COTTON.value, **kwargs):
        """
        Initialize this instance of Reindeer.

        :param name: a string
        :param description: a string
        :param product_id: a string
        :param size: a string
        :param has_glow: boolean
        :param stuffing: a string
        :param fabric: a string
        """

        super().__init__(name, description, product_id, stuffing, size, fabric)
        self._has_glow = has_glow
        self.inventory_key = "rd"

    def get_has_glow(self):
        """
        Return nose attribute of this instance of Reindeer.

        :return: a boolean, true if nose glows, else false
        """
        return self._has_glow

    def __str__(self):
        """
        Generate a string representation of this instance of Reindeer.

        :return: a string representation of DancingSkeleton
        """
        return "Item StuffedAnimal, Product ID: {}, Name: {}, Nose Glows: {}," \
               " Size {}, Stuffing: {}, Fabric: {}".format(self.get_product_id(),
                                                           self.get_name(), self.get_has_glow(),
                                                           self.size, self.stuffing_type, self.fabric)


class EasterBunny(StuffedAnimals):
    """
    Represent an Easter Bunny which extends the abstract class StuffedAnimals
    """

    def __init__(self, name: str, description: str,
                 product_id: str, size: str, colour: str,
                 stuffing=StuffingType.POLY.value, fabric=FabricType.LINEN.value, **kwargs):
        """
        Initialize this instance of EasterBunny.

        :param name: a string
        :param description: a string
        :param product_id: a string
        :param size: a string
        :param colour: a string
        :param stuffing: a string, default value of Polyester
        :param fabric: a string, default value of Linen
        """

        super().__init__(name, description, product_id, stuffing, size, fabric)
        self.colour = colour
        self.inventory_key = "eb_" + str(colour)

    @property
    def colour(self):
        """
        Return the color of this instance of Stuffed Animal.

        :return: a string representing color
        """
        return self._colour

    @colour.setter
    def colour(self, colour):
        """
        Set the color for this instance of Easter Bunny.

        :param colour: a string
        :precondition color: must be either "white", "grey", "pink" or "blue"
        """
        if colour not in [e.value for e in EasterBunnyColours]:
            raise InvalidDataError(UIMessage.stuffed_animal_error())

        self._colour = colour

    def __str__(self):
        """
        Generate a string representation of this instance of Easter Bunny.

        :return: a string representation of DancingSkeleton
        """
        return "Item StuffedAnimal, Product ID: {}, Name: {}, Color: {}," \
               " Size {}, Stuffing: {}, Fabric: {}".format(self.get_product_id(),
                                                           self.get_name(), self.colour,
                                                           self.size, self.stuffing_type, self.fabric)
