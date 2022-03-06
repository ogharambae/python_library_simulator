from enum import Enum


class ToffeeVariety(Enum):
    """
    Enum class which represents various Toffee Varieties.
    """

    salt = "sea salt"
    reg = "regular"


class CandyCaneVariety(Enum):
    """
    Enum class which represents various CandyCane Varieties.
    """

    red = "red"
    green = "green"


class StuffingType(Enum):
    """
    An enum class with all stuffing types used in StuffedAnimal Class.
    """

    poly = "polyester fiberfill"
    wool = "wool"


class FabricType(Enum):
    """
    An enum class with all fabric types used in StuffedAnimal Class.
    """

    linen = "linen"
    cotton = "cotton"
    acrylic = "acrylic"


class SizeOptions(Enum):
    """
    An enum class representing all the sizes of a StuffedAnimal.
    """

    sm = "small"
    med = "medium"
    lrg = "large"


class EasterBunnyColors(Enum):
    """
    An enum class representing the possible colors
    of an EasterBunny Stuffed Animal
    """
    white = "white"
    grey = "grey"
    pink = "pink"
    blue = "blue"


class SpiderType(Enum):
    """
    An enum class that represents the various Spider Types of an RC Spider.
    """
    tarantula = "tarantula"
    wolf = "wolf spider"


class RobotBunnyColor(Enum):
    """
    An enum class that represents the various colors of a RobotBunny.
    """
    orange = "orange"
    blue = "blue"
    pink = "pink"
