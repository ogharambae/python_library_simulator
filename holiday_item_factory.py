from candy_types import PumpkinCaramelToffee, CandyCane, CremeEgg
from stuffed_animal_types import DancingSkeleton, Reindeer, EasterBunny
from toy_types import RCSpider, SantaWorkshop, RobotBunny
from item_enum import ItemEnum
from invalid_data_error import InvalidDataError


class HalloweenItemFactory:
    """
    Represents a Halloween Item Factory mapping based on item type enum
    """

    @staticmethod
    def get_item_factory(item_type):
        match item_type:
            case ItemEnum.CANDY.value:
                return PumpkinCaramelToffee
            case ItemEnum.ANIMAL.value:
                return DancingSkeleton
            case ItemEnum.TOY.value:
                return RCSpider
            case _:
                raise InvalidDataError("No matching item type found (%s)" % item_type)


class ChristmasItemFactory:
    """
    Represents a Christmas Item Factory mapping based on item type enum
    """

    @staticmethod
    def get_item_factory(item_type):
        match item_type:
            case ItemEnum.CANDY.value:
                return CandyCane
            case ItemEnum.ANIMAL.value:
                return Reindeer
            case ItemEnum.TOY.value:
                return SantaWorkshop
            case _:
                raise InvalidDataError("No matching item type found (%s)" % item_type)


class EasterItemFactory:
    """
    Represents a Easter Item Factory mapping based on item type enum
    """

    @staticmethod
    def get_item_factory(item_type):
        match item_type:
            case ItemEnum.CANDY.value:
                return CremeEgg
            case ItemEnum.ANIMAL.value:
                return EasterBunny
            case ItemEnum.TOY.value:
                return RobotBunny
            case _:
                raise InvalidDataError("No matching item type found (%s)" % item_type)
