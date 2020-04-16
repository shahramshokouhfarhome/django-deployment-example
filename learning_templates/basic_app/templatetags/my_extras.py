# learning_templates\basic_app\templatetags\my_extras.py
from django import template

register = template.Library()

# Using a decorator to register
@register.filter(name='cut200')
def cut20(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, '')

# register.filter('cut200', cut20)
