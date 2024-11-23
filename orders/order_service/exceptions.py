# Exception to signal that an order does not exist
class OrderNotFoundError(Exception):
    pass

# Exception tp signal that an API integration error has taken place
class APIIntegrationError(Exception):
    pass

# Exception to signal that the action being performed is invalid
class InvalidActionError(Exception):
    pass