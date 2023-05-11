from django import template
from django.forms.models import model_to_dict

register = template.Library()

@register.filter(name="get_item")
def get_dict_item(model_obj, key):
    dictionary = model_to_dict(model_obj)
    return dictionary.get(key)