from enum import Enum


class StuffingType(Enum):
    """
    An enum class with all stuffing types used in StuffedAnimal Class.
    """

    poly = "Polyester Fiberfill"
    wool = "Wool"


class FabricType(Enum):
    """
    An enum class with all fabric types used in StuffedAnimal Class.
    """

    linen = "Linen"
    cotton = "Cotton"
    acrylic = "Acrylic"
