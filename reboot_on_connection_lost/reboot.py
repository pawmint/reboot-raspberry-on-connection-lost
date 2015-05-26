import requests
import os
import time
from datetime import datetime
import sys
from threading import Timer
from appdirs import user_log_dir


def check_connection(url='http://www.google.com', timeout=5):
    while True:
        try:
            requests.get(url, timeout=timeout)
            yield True
        except Exception:
            yield False


def ensure_shutdown_dir():
    try:
        os.stat(user_log_dir('reboot_on_connexion_lost', 'pawmint'))
    except:
        os.makedirs(user_log_dir('reboot_on_connexion_lost', 'pawmint'))

def shutdown():
    with open(os.path.join(user_log_dir("reboot_on_connexion_lost", "pawmint"), "shutdown.txt"), "a") as myfile:
        myfile.write(datetime.now().strftime('%Y%m%d_%H%M\n'))
    os.system("shutdown now -r")


def main():
    ensure_shutdown_dir()
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
