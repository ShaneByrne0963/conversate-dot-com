from django import template
from django.shortcuts import get_object_or_404
from forum.models import Poll


register = template.Library()

@register.simple_tag
def poll_status(poll_id, user_id):
    """
    Gets the status of the poll:
    -1: The poll is closed and the user has not voted
    0: The poll is open and the user has not voted
    >1: The user has voted for the answer number that is returned
    """
    print('ID: ', poll_id)
    poll = get_object_or_404(Poll, id=int(poll_id))
    answers = list(poll.answers.all())
    for answer in answers:
        if answer.votes.filter(id=user_id).exists():
            return answer.position
    return -1 if poll.has_expired() else 0
