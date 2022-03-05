from Item import Toys


class SantaWorkshop(Toys):
    """
    Represent a Santa Workshop Toy, extending the abstract class Toy,
    with dimensions, and number of rooms.
    """

    def __init__(self, name: str, description: str,
                 product_id: str, min_age: int, dimensions, num_rooms: int, has_battery=False):
        """
        Initialize this instance of Santa's Workshop.

        :param name: a string representing name
        :param description: a string representing a description
        :param product_id: a string
        :param min_age: an int
        :param dimensions: an int
        :param num_rooms: an int
        :param has_battery: a boolean, default value is false
        """

        super().__init__(name, description, product_id, has_battery, min_age)
        self._dimensions = dimensions
        self._num_rooms = num_rooms

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


class RCSpider(Toys):
    """
    Represent a remote control spider, which extends the abstract class Toys.
    """

    ## MAY BE ANOTHER PLACE WHERE AN ENUM MAKES SENSE FOR SPIDER TYPE
    def __init__(self, name: str, description: str,
                 product_id: str, min_age: int, speed, jump_height, glows_in_dark,
                 spider_type, has_battery=True):
        """
        Initialize this instance of RC Spider.

        :param name: a string representing name
        :param description: a string
        :param product_id: a string
        :param min_age: an int
        :param speed: a float
        :param jump_height: a float
        :param glows_in_dark: boolean, True if glows in dark. else False
        :param spider_type: String either Tarantula or a Wolf Spider
        :param has_battery: Boolean, default True
        """

        super().__init__(name, description, product_id, has_battery, min_age)
        self._speed = speed
        self._jump_height = jump_height
        self._glows = glows_in_dark
        self._spider_type = spider_type

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
        return self._glows

    def spider_type(self):
        """
        Return the spider type of this RC Spider.

        :return: a string
        """
        return self._spider_type


class RobotBunny(Toys):
    """
    Represent a Robot Bunny, which extends the abstract class Toys.
    """
    ## MAY BE ANOTHER PLACE WHERE AN ENUM MAKES SENSE FOR color (orange, blue or pink)
    def __init__(self, name: str, description: str,
                 product_id: str, min_age: int, num_sound_effects: int,
                 color, has_battery=True):
        """
        Initialize this instance of Robot Bunny

        :param name: a string
        :param description: a string
        :param product_id: a string
        :param min_age: an int
        :param num_sound_effects: an int
        :param color: a string
        :param has_battery: a boolean, default value True
        """

        super().__init__(name, description, product_id, has_battery, min_age)
        self._num_sound_effects = num_sound_effects
        self._color = color

    def get_num_sound_effects(self):
        """
        Return the number of sound effects for this instance of Robot Bunny.

        :return: an int
        """
        return self._num_sound_effects

    def get_color(self):
        """
        Return the color of this instance of Robot Bunny.

        :return: a string
        """
        return self._color
