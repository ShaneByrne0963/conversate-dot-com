from datetime import datetime


def get_time_elapsed(date):
    """
    Returns a string stating how long it has been since the specified date
    """
    current_time = datetime.now().timestamp()
    previous_time = date.timestamp()
    elapsed_time = current_time - previous_time
    if elapsed_time < 60:
        return 'Just now'
    time_value = 0
    time_type = ''
    # Minutes
    if elapsed_time < 3600:
        time_value = elapsed_time // 60
        time_type = 'minute'
    # Hours
    elif elapsed_time < 86400:
        time_value = elapsed_time // 3600
        time_type = 'hour'
    # Days
    elif elapsed_time < 604800:
        time_value = elapsed_time // 86400
        time_type = 'day'
    # Weeks
    elif elapsed_time < 3024000:
        time_value = elapsed_time // 604800
        time_type = 'week'
    # Months
    elif elapsed_time < 31536000:
        time_value = elapsed_time // 2592000
        time_type = 'month'
    # Years
    else:
        time_value = elapsed_time // 31536000
        time_type = 'year'
    time_value = int(time_value)
    if time_value != 1:
        time_type += 's'
    return f'{time_value} {time_type} ago'
