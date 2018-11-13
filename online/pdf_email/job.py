from threading import Timer
from .pdf_TorF import main, len_pdf
import datetime


def now_time2(a=0):
    now = datetime.datetime.now()
    delta = datetime.timedelta(minutes=a)
    n_days = now + delta
    print(n_days.strftime('%Y-%m-%d %H:%M:%S'))
    f = n_days.strftime('%H')
    i = int(f)
    return i


def say_work():
    time = now_time2()
    num = len(len_pdf())
    if 6 > time >= 22 and num > 50:
        main()
        t = Timer(1*60*60, say_work)
        t.start()
    elif time == 23:
        if num == 0:
            t = Timer(1 * 60 * 60, say_work)
            t.start()
        else:
            main()
            t = Timer(1*60*60, say_work)
            t.start()
    else:
        print("Hello World")
        t = Timer(1*60*60, say_work)
        t.start()


def printHello():
    print("Hello World")
    t = Timer(2, printHello)
    t.start()


def work():
    time = now_time2()
    num = len(len_pdf())
    if 6 > time >= 22 and num > 50:
        main()
        # t = Timer(1*60*60, say_work)
        # t.start()
    elif time == 23:
        if num == 0:
            # t = Timer(1 * 60 * 60, say_work)
            # t.start()
            pass
        else:
            main()
            # t = Timer(1*60*60, say_work)
            # t.start()
    else:
        print("Hello World")
        # t = Timer(1*60*60, say_work)
        # t.start()


if __name__ == "__main__":
    work()


