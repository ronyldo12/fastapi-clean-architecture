from exceptions.app_exception import AppException
class ValidationException(AppException):
    code: int = 422