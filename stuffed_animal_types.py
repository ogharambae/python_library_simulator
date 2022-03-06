from Item import StuffedAnimals
from item_enum import StuffingType, FabricType, EasterBunnyColors
from invalid_data_error import InvalidDataError
from ui_message import UIMessage


class DancingSkeleton(StuffedAnimals):
    """
    Represent a dancing skeleton, which extends the abstract class of
    StuffedAnimals
    """

    # Unsure if Dancing Skeleton glows in the dark by default!
    def __init__(self, name: str, description: str,
                 product_id: str, size: str, glows_in_dark: bool,
                 stuffing=StuffingType.poly.value, fabric=FabricType.acrylic.value):
        """
        Initialize this instance of Dancing Skeleton.

        :param name: a string
        :param description: a string
        :param product_id: a string
        :param size: a string
        :param glows_in_dark: a boolean, true if Glows in dark
        :param stuffing: a string
        :param fabric: a string
        """

        super().__init__(name, description, product_id, stuffing, size, fabric)
        self._glows_in_dark = glows_in_dark

    def get_glows_in_dark(self):
        """
        Return whether this Dancing Skeleton glows in dark.

        :return: a boolean
        """
        return self._glows_in_dark

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
                 product_id: str, size: str, nose_glows: bool,
                 stuffing=StuffingType.wool.value, fabric=FabricType.cotton.value):
        """
        Initialize this instance of Reindeer.

        :param name: a string
        :param description: a string
        :param product_id: a string
        :param size: a string
        :param nose_glows: boolean
        :param stuffing: a string
        :param fabric: a string
        """

        super().__init__(name, description, product_id, stuffing, size, fabric)
        self._nose_glows = nose_glows

    def get_nose_glow(self):
        """
        Return nose attribute of this instance of Reindeer.

        :return: a boolean, true if nose glows, else false
        """
        return self._nose_glows

    def __str__(self):
        """
        Generate a string representation of this instance of Reindeer.

        :return: a string representation of DancingSkeleton
        """
        return "Item StuffedAnimal, Product ID: {}, Name: {}, Nose Glows: {}," \
               " Size {}, Stuffing: {}, Fabric: {}".format(self.get_product_id(),
                                                           self.get_name(), self.get_nose_glow(),
                                                           self.size, self.stuffing_type, self.fabric)


class EasterBunny(StuffedAnimals):
    """
    Represent an Easter Bunny which extends the abstract class StuffedAnimals
    """

    def __init__(self, name: str, description: str,
                 product_id: str, size: str, color: str,
                 stuffing=StuffingType.poly.value, fabric=FabricType.linen.value):
        """
        Initialize this instance of EasterBunny.

        :param name: a string
        :param description: a string
        :param product_id: a string
        :param size: a string
        :param color: a string
        :param stuffing: a string, default value of Polyester
        :param fabric: a string, default value of Linen
        """

        super().__init__(name, description, product_id, stuffing, size, fabric)
        self.color = color

    @property
    def color(self):
        """
        Return the color of this instance of Stuffed Animal.

        :return: a string representing color
        """
        return self._color

    @color.setter
    def color(self, color):
        """
        Set the color for this instance of Easter Bunny.

        :param color: a string
        :precondition color: must be either "white", "grey", "pink" or "blue"
        """
        if color.lower() not in (EasterBunnyColors.white.value, EasterBunnyColors.grey.value,
                                 EasterBunnyColors.pink.value, EasterBunnyColors.blue.value):
            raise InvalidDataError(UIMessage.stuffed_animal_error())

        self._color = color

    def __str__(self):
        """
        Generate a string representation of this instance of Easter Bunny.

        :return: a string representation of DancingSkeleton
        """
        return "Item StuffedAnimal, Product ID: {}, Name: {}, Color: {}," \
               " Size {}, Stuffing: {}, Fabric: {}".format(self.get_product_id(),
                                                           self.get_name(), self.color,
                                                           self.size, self.stuffing_type, self.fabric)
