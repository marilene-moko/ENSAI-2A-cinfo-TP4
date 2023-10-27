from prompt_toolkit.validation import ValidationError, Validator


class Validation(Validator):
    def validate_email(self, document):
        if not len(document.text) > 0:
            raise ValidationError(
                message="Input cannot be empty.",
                cursor_position=document.cursor_position,
            )

    def validate_pas_nul(self, document):
        if not len(document.text) > 0:
            raise ValidationError(
                message="Input cannot be empty.",
                cursor_position=document.cursor_position,
            )
