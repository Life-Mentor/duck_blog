from django import template
from blog.models import Catgory

register = template.Library()

@register.simple_tag
def get_category_list():
    return Catgory.objects.all()

