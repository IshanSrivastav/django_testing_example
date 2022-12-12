from django import template

register = template.Library()

@register.filter(name='cul')
def cul(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')


# register.filter('cul', cul)