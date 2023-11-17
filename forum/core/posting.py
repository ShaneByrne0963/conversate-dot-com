def convert_post_content(content_input):
    """
    Converts a string input into HTML, adding <p> tags for each line
    """
    if not isinstance(content_input, str):
        raise TypeError("content_input must be a string")
    input_lines = content_input.split('\n')

    formatted_input = ''
    has_line_break = False
    for line in input_lines:
        line = line.strip()
        if line == '':
            if not has_line_break:
                formatted_input += '<br>'
                has_line_break = True
        else:
            formatted_input += f'<p>{line}</p>'
            has_line_break = False

    return formatted_input
