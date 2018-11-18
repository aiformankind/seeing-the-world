import datetime


def get_unique_time():
    """
    Get current time and format to YYYYMMDDMMSS(000000-999999)

    :return: type(str)
    """
    this_now = datetime.datetime.now()
    return this_now.strftime("%Y%M%d%H%S%f")
