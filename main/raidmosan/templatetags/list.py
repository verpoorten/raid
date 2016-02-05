from django import template


register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_itemlabel(dictionary, key):
    label = str(dictionary.get(key))
    label=label.strip('["')
    label=label.strip('"]')
    return "   "+label+"   "
