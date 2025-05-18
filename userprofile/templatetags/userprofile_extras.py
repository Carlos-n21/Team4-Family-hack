from django import template

register = template.Library()

@register.filter
def replace(value, arg):
    """Replaces all occurrences of the first arg with the second arg in the string."""
    old, new = arg.split(',')
    return value.replace(old, new)
