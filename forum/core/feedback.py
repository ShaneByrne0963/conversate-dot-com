from django.contrib import messages


def deny_access(request):
    """
    Adds an error message that notifies the user they are not allowed to
    perform a specific action
    """
    messages.add_message(
        request,
        messages.ERROR,
        'You do not have permission to perform that action'
    )