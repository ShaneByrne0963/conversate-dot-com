def convert_post_content(content_input):
    """
    Converts a string input into HTML, adding <p> tags for each line
    """
    if not isinstance(content_input, str):
        raise TypeError("content_input must be a string")
    input_lines = content_input.split('\n')

    formatted_input = ''
    for line in input_lines:
        formatted_input += f'<p>{line}</p>'
    formatted_input = formatted_input.replace('<p></p>', '<br>')

    return formatted_input
