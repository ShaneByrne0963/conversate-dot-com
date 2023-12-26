from django.contrib import messages


def display_error(request, message):
    """
    Adds an error to the list of messages to be displayed to the user
    """
    messages.add_message(
        request,
        messages.ERROR,
        message
    )


def deny_access(request):
    """
    Adds an error message that notifies the user they are not allowed to
    perform a specific action
    """
    display_error(request,'You do not have permission to perform that action')
