from django import template
from main.models import Category

register = template.Library()


@register.simple_tag()
def tag_categories():
    return Category.objects.all()



