class InvalidDataError(Exception):
    """Exception triggered when provided inventory information is incorrect."""

    def __init__(self, message):
        self.message = message
    pass
