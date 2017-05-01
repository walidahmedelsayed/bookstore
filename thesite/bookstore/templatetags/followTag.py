from django import template
from django.template import Template

register = template.Library()


@register.simple_tag(takes_context=True)
def get_follow(context,user, author):
    if author.authorfollow_set.count() == 0:
        return Template('<i class="add user large  icon"></i><span>Follow</span>').render(context)
    for status in author.authorfollow_set.all():
        if status.profile_id == user.id and status.followStatus == 0:
            return Template('<i class="add user large  icon"></i><span>Follow</span>').render(context)
        elif status.profile_id == user.id and status.followStatus == 1:
            return Template('<i class="remove user large  icon"></i><span>Un Follow</span>').render(context)

    return Template('<i class="add user large  icon"></i><span>Follow</span>').render(context)
