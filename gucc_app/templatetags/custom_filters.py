from django import template
import logging

logger = logging.getLogger(__name__)
register = template.Library()

@register.simple_tag
def get(pool, attr):
    return getattr(pool, attr).all()

@register.filter
def get_field_value(obj, field_name):
    
    return getattr(obj, field_name)

@register.filter
def get_field_value(item, field_name):
    try:
        field_name = field_name.lower()
        return getattr(item, field_name)
    except AttributeError as e:
        logger.error(f"Error getting field value for item {item} and field {field_name}: {e}")
        return f"Error: {field_name} not found for item {item}"

@register.simple_tag
def get_kitheaders(kitheaders, type):
    return kitheaders.get(type, [])

@register.simple_tag
def get_related_objects(pool, type):
    return pool.get_related_objects(type)

@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)

@register.simple_tag
def define(val=None):
  return val