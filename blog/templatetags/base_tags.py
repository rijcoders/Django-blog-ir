from django import template

from blog.models import Article, Category

register = template.Library()

@register.simple_tag
def title():
   return "RIJ Blog" 

@register.inclusion_tag("blog/partials/category_navbar.html")
def category_navbar():
    return {
        'category': Category.objects.filter(status=True)
    }