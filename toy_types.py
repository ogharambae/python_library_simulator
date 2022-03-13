from item import Toys
from item_enum import SpiderType, RobotBunnyColour
from invalid_data_error import InvalidDataError
from ui_message import UIMessage


class SantaWorkshop(Toys):
    """
    Represent a Santa Workshop Toy, extending the abstract class Toy,
    with dimensions, and number of rooms.
    """

    def __init__(self, name: str, description: str,
                 product_id: str, min_age: int, dimensions, num_rooms: int, has_batteries=False, **kwargs):
        """
        Initialize this instance of Santa's Workshop.

        :param name: a string representing name
        :param description: a string representing a description
        :param product_id: a string
        :param min_age: an int
        :param dimensions: an int
        :param num_rooms: an int
        :param has_batteries: a boolean, default value is false
        """

        super().__init__(name, description, product_id, has_batteries, min_age)
        self._dimensions = dimensions
        self._num_rooms = num_rooms
        self.inventory_key = "sw"

    def get_dimensions(self):
        """
        Return the dimensions, width and height, of this instance of Santa's Work Shop.

        :return: dimensions of this instance of Santa's Workshop
        """
        return self._dimensions

    def get_num_rooms(self):
        """
        Return the number of rooms for this instance of Santa's Work Shop.

        :return: an int
        """
        return self._num_rooms

    def __str__(self):
        """
        Generate a String representation of this instance of Santa's Workshop.

        :return: a string
        """

        return "Item Toy, Product ID: {}, Name: {}, Recommended Age: {}," \
               "Dimensions: {}, Number of Rooms: {}, No Batteries Required ".format(self.get_product_id(),
                                                                                    self.get_name(),
                                                                                    self.get_min_age(),
                                                                                    self.get_dimensions(),
                                                                                    self.get_num_rooms())


class RCSpider(Toys):
    """
    Represent a remote control spider, which extends the abstract class Toys.
    """

    def __init__(self, name: str, description: str,
                 product_id: str, min_age: int, speed, jump_height, has_glow,
                 spider_type, has_battery=True, **kwargs):
        """
        Initialize this instance of RC Spider.

        :param name: a string representing name
        :param description: a string
        :param product_id: a string
        :param min_age: an int
        :param speed: a float
        :param jump_height: a float
        :param has_glow: boolean, True if glows in dark. else False
        :param spider_type: String either Tarantula or a Wolf Spider
        :param has_battery: Boolean, default True
        """

        super().__init__(name, description, product_id, has_battery, min_age)
        self._speed = speed
        self._jump_height = jump_height
        self._has_glow = has_glow
        self.spider = spider_type
        self.inventory_key = "rcs_" + str(spider_type)

    def get_speed(self):
        """
        Return the movement speed of this instance of RC Spider.

        :return: a float representing RC Spider speed
        """
        return self._speed

    def get_jump_height(self):
        """
        Return the jump height of this instance of RC Spider.

        :return: a float representing jump height of this RC Spider
        """
        return self._jump_height

    def get_glows_in_dark(self):
        """
        Return whether this RC Spider glows in the dark.

        :return: a boolean, true if glows in the dark, else False
        """
        return self._has_glow

    @property
    def spider(self):
        """
        Return the spider type of this RC Spider.

        :return: a string
        """
        return self._spider_type

    @spider.setter
    def spider(self, spider_type: str):
        """
        Set the type of spider of this RC Spider.

        :param spider_type: a string
        :precondition spider_type: must be either a "Tarantula" or a "Wolf Spider"
        """
        if spider_type.lower() not in [e.value for e in SpiderType]:
            raise InvalidDataError(UIMessage.spider_type_error_message())

        self._spider_type = spider_type

    def __str__(self):
        """
        Generate a String representation of this instance of RC Spider.

        :return: a string
        """

        return "Item Toy, Product ID: {}, Name: {}, Recommended Age: {}," \
               " Speed: {}, Jump Height {}, Glows in Dark: {}, " \
               "Spider Type: {}".format(self.get_product_id(), self.get_name(),
                                        self.get_min_age(), self.get_speed(),
                                        self.get_jump_height(),
                                        self.get_glows_in_dark(),
                                        self.spider)


class RobotBunny(Toys):
    """
    Represent a Robot Bunny, which extends the abstract class Toys.
    """

    def __init__(self, name: str, description: str,
                 product_id: str, min_age: int, num_sound: int,
                 colour, has_battery=True, **kwargs):
        """
        Initialize this instance of Robot Bunny

        :param name: a string
        :param description: a string
        :param product_id: a string
        :param min_age: an int
        :param num_sound: an int
        :param colour: a string
        :param has_battery: a boolean, default value True
        """

        super().__init__(name, description, product_id, has_battery, min_age)
        self._num_sound = num_sound
        self._colour = colour
        self.inventory_key = "rb_" + str(colour)

    def get_num_sound_effects(self):
        """
        Return the number of sound effects for this instance of Robot Bunny.

        :return: an int
        """
        return self._num_sound

    @property
    def colour(self):
        """
        Return the color of this instance of Robot Bunny.

        :return: a string
        """
        return self._colour

    @colour.setter
    def colour(self, colour: str):
        """
        Set the color of this instance of RobotBunny.

        :param colour: a string
        :precondition color: must be either "Orange", "Blue", or "Pink"
        """
        if colour not in [e.value for e in RobotBunnyColour]:
            raise InvalidDataError(UIMessage.robot_bunny_colour_error_message())
        self._colour = colour

    def __str__(self):
        """
        Generate a String representation of this instance of Robot Bunny.

        :return: a string
        """

        return "Item Toy, Product ID: {}, Name: {}, Recommended Age: {}," \
               "Num of Sound Effects: {}, Color {}".format(self.get_product_id(), self.get_name(),
                                                           self.get_min_age(),
                                                           self.get_num_sound_effects(), self.colour)
