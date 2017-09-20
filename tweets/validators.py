from django.core.exceptions import ValidationError

def empty_conent(value):
    content = value
    if content == '':
        raise ValidationError('Content cannot be empty')

    return content
