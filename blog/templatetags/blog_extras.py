from django.contrib.auth.models import User
from django import template

# this instance can registers filters
register = template.Library()

# it register the filter by using decorators.
@register.filter
def author_details(author):
    if not isinstance(author, User):
        # return empty string as safe default
        return ""

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    return name