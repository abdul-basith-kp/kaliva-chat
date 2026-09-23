
from validators.general_validator import GeneralValidator
from exceptions import ValidationError

class UserValidator:

    def __init__(self, general_validator: GeneralValidator) -> None:
        self.gv = general_validator

    def validate_name(self, name: str) -> None:
        self.gv.validate_blank_input(name=name)
        if len(name) < 4:
            raise ValidationError('name too short')
        elif len(name) > 16:
            raise ValidationError("name too long")

    def validate_password(self, password: str) -> None:
        self.gv.validate_blank_input(password=password)
        if len(password) < 4:
            raise ValidationError('password too short')
        elif len(password) > 16:
            raise ValidationError("password too long")