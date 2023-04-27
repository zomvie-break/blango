from django.contrib.auth.models import User
from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

# this instance can registers filters
register = template.Library()

# it register the filter by using decorators.
@register.filter
def author_details(author):
    if not isinstance(author, User):
        # return empty string as safe default
        return ""

    if author.first_name and author.last_name:
        name = escape(f"{author.first_name} {author.last_name}")
    else:
        name = escape(f"{author.username}")

    if author.email:
      email = author.email
      prefix = f'<a href="mailto:{email}">'
      suffix = "</a>"
    else:
      prefix=''
      sufix=''

    return mark_safe(f'{prefix}{name}{suffix}')