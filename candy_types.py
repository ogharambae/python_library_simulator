from Item import Candy


class PumpkinCaramelToffee(Candy):
    """
    Represent a piece of Pumpkin Caramel Toffee, extending abstract
    class of Candy.
    """

    def __init__(self, name: str, description: str,
                 product_id: str, variety, has_nuts= True, has_lactose=True):
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
        self._variety = variety

    def get_variety(self):
        """
        Return the variety of this Pumpkin Caramel Toffee.

        :return: a string representing variety of Pumpkin Caramel Toffee
        """
        return self._variety


class CandyCane(Candy):
    """
    Represent a Candy Cane, which extends the abstract class of Candy.
    """

    def __init__(self, name: str, description: str,
                 product_id: str, stripes: str, has_nuts=False, has_lactose=False):
        """
        Initialize this instance of CandyCane.

        :param name: a string
        :param description: a string
        :param product_id: a string
        :param stripes: a string, either "Red" or "Green"
        :param has_nuts: A boolean False by default
        :param has_lactose: a boolean False by default
        """
        super().__init__(name, description, product_id, has_nuts, has_lactose)
        self._stripes = stripes

    def get_stripes(self):
        """
        Return the stripe color of this instance of CandyCane.

        :return: a string, either "Red" or "Green"
        """
        return self._stripes


class CremeEgg(Candy):
    """
    Represent a CremeEgg, which extends the abstract class of Candy.
    """
    def __init__(self, name: str, description: str,
                 product_id: str, pack_size: int, has_nuts=True, has_lactose=True):
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
        self._pack_size = pack_size

    def get_pack_size(self):
        """
        Return the pack size of this instance of CremeEgg.

        :return: an int representing the pack size of CremeEgg
        """
        return self._pack_size





