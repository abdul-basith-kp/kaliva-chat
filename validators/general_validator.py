
from exceptions import ValidationError

class GeneralValidator:
    @staticmethod
    def validate_blank_input(**inputs) -> None:
        for key, value in inputs.items():
            if value.strip() == '':
                raise ValidationError(f"{key} cannot be blank")