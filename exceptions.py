
class ApplicationError(Exception):
    pass

class ValidationError(ApplicationError):
    pass

class AuthenticationError(ApplicationError):
    pass

class DatabaseConnectionError(ApplicationError):
    pass

class DatabaseDataCreationError(ApplicationError):
    pass

class DatabaseFetchingError(ApplicationError):
    pass
class MessageFetchingError(ApplicationError):
    pass
class MessageCreationError(ApplicationError):
    pass