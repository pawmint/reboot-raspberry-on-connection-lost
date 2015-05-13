import requests
import os
import time
import sys
from threading import Timer


def check_connection(url='http://www.google.com', timeout=5):
    while True:
        try:
            requests.get(url, timeout=timeout)
            yield True
        except requests.ConnectionError:
            yield False


def shutdown():
    os.system("shutdown now -h")


def main():
    is_timer_running = False
    timer = None
    if len(sys.argv) == 2:
        timer_duration = int(sys.argv[1])
    else:
        timer_duration = 3600

    for has_connection in check_connection():
        if has_connection and is_timer_running:
            timer.cancel()
            is_timer_running = False
        elif not (has_connection or is_timer_running):
            timer = Timer(timer_duration, shutdown)
            timer.start()
            is_timer_running = True
        time.sleep(10)


if __name__ == '__main__':
    main()
