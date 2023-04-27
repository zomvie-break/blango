from django.contrib.auth.models import User
from django import template
from django.utils.html import format_html
# this instance can registers filters
register = template.Library()

# it register the filter by using decorators.
@register.filter
def author_details(author, current_user=None):
    if not isinstance(author, User):
        # return empty string as safe default
        return ""

    if author == current_user:
      return format_html('<strong>me</strong>')

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
      email = author.email
      prefix = format_html('<a href="mailto:{}">', email)
      suffix = format_html('</a>')
    else:
      prefix=''
      sufix=''

    return format_html('{}{}{}', prefix, name, suffix)

@register.simple_tag
def row(extra_classes=''):
  return format_html('<div class="row {}">', extra_classes)

@register.simple_tag
def endrow():
  return format_html('</div>')