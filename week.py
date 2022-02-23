import datetime
def weeker():
    today = datetime.datetime.today().strftime("%W")

    if int(today) % 2 == 0:
        return 1
    else:
        return 0
