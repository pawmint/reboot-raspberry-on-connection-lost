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
    TIMER_DURATION = 3600
    FREQUENCY_CHECK = 10
    if len(sys.argv) == 3:
        TIMER_DURATION = int(sys.argv[1])
        FREQUENCY_CHECK = int(sys.argv[2])

    for has_connection in check_connection():
        if has_connection and is_timer_running:
            timer.cancel()
            is_timer_running = False
        elif not (has_connection or is_timer_running):
            timer = Timer(TIMER_DURATION, shutdown)
            timer.start()
            is_timer_running = True
        time.sleep(FREQUENCY_CHECK)


if __name__ == '__main__':
    main()
