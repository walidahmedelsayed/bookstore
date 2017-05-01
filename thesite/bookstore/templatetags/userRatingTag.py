from django import template
from django.template import Template

register = template.Library()


@register.simple_tag(takes_context=True)
def get_user_rate(context,user, book):
    if book.rating_set.count() == 0:
        return Template('<div class="ui large star rating"  data-id="'+str(book.id)+'" data-rating="0"></div>').render(context)
    for rate in book.rating_set.all():
        if rate.profile_id == user.id :
            return Template('<div class="ui large star rating"  data-id="'+str(book.id)+'" data-rating="'+str(rate.rate)+'"></div>').render(context)

    return Template('<div class="ui large star rating"  data-id="'+str(book.id)+'" data-rating="0"></div>').render(context)
