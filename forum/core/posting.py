def convert_post_content(content_input):
    if not isinstance(content_input, str):
        raise TypeError("content_input must be a string")
    input_lines = content_input.split('\n')
    formatted_input = ''
    for line in input_lines:
        formatted_input += f'<p>{line}</p>'
    return formatted_input
