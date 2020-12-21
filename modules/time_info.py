from datetime import datetime


def time():
    current_datetime = datetime.now()
    print(str(current_datetime.hour) + ":" + str(current_datetime.minute))