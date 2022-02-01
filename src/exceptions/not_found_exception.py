from exceptions.app_exception import AppException

class NotFoundException(AppException):
    code: int = 404