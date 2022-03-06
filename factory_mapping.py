from enum import Enum
from holiday_item_factory import HalloweenItemFactory, ChristmasItemFactory, EasterItemFactory
from invalid_data_error import InvalidDataError


class Holiday(Enum):
    """
    Enum class which represents various Holiday types.
    """
    HALLOWEEN = "halloween"
    CHRISTMAS = "christmas"
    EASTER = "easter"


class FactoryMapping:
    """
    Represents a Factory Mapping class to return the correct factory class based on holiday and item type
    """

    @staticmethod
    def get_item_factory(holiday, item_type):
        match holiday:
            case Holiday.HALLOWEEN:
                return HalloweenItemFactory.get_item_factory(item_type)
            case Holiday.CHRISTMAS:
                return ChristmasItemFactory.get_item_factory(item_type)
            case Holiday.EASTER:
                return EasterItemFactory.get_item_factory(item_type)
            case _:
                raise InvalidDataError("No matching holiday found (%s)" % holiday)
