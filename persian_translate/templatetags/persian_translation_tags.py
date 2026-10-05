from django import template

register = template.Library()

@register.filter
def translate_number(value):
    value = str(value)
    english_to_persian_table = value.maketrans('0123456789', '۰١٢٣٤٥٦٧٨٩')

    return value.translate(english_to_persian_table)
@register.filter
def price_comma(value):
    value = str(value)
    return (value[:3]+ ',' + value[3:])

