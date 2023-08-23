from django import template 
from django.shortcuts import redirect
from django.urls import reverse


register = template.Library()


@register.simple_tag(takes_context=True)
def prevent_login(context):
    user = context['user']
    if user.is_authenticated:
        return reverse('home:home')
    return None 
