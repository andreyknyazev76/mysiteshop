from django import template
from django.utils.http import urlencode
from blog.models import Post


register = template.Library()


@register.simple_tag()
def tag_post():
    return Post.objects.all()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)