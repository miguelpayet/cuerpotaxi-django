import markdown2
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def mi_markdown(value):
    return mark_safe(markdown2.markdown(force_text(value), safe_mode=True))
