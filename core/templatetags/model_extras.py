from django.template import Library

register = Library()

@register.filter
def model_name(obj):
    """
    Returns the name of the model for the object.
    """
    return obj._meta.verbose_name
