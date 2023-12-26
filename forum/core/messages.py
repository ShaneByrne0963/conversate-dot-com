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


def display_form_errors(request, form):
    """
    Adds an error message for each error found in a form
    """
    if form.errors:
        error_text = form.errors.as_text()
        error_messages = error_text.split('\n*')
        for error in error_messages:
            # Separating the field from the message
            error = error.replace('*', '')
            error_properties = error.split('\n')
            error_message = error_properties[1].strip()

            # Replacing "This field is required" message to be more specific
            if 'required' in error_message:
                if 'password' in error_properties[0]:
                    error_message = error_message.replace('This', 'Password')
            display_error(request, error_message)
