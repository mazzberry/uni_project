from django import template

register = template.Library()

@register.filter
def only_active_comments(comments):
    return comments.filter(active=True) #vid 217 || comments.exclude(active=False)

