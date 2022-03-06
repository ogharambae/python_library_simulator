class Order:
    """
    Represent the Order object which contains the detail of an order
    """

    def __init__(self, **kwargs) -> None:
        item_factory = kwargs["factory_method"]
        item = item_factory(kwargs)
        pass
