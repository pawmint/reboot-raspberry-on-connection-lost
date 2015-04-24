import requests
import os
import time


def check_connection(url='8.8.8.8', timeout=5):
    while True:
        try:
            _ = requests.get(url, timeout=timeout)
            yield True
        except requests.ConnectionError:
            yield False


def shutdown():
    os.system("shutdown now -h")


def main():
    for has_connection in check_connection():
        if has_connection and is_timer_running:
            timer.cancel()
            is_timer_running = False
        elif not (has_connection or is_timer_running):
            timer = Timer(3600, shutdown)
            timer.start()
            is_timer_running = True
        time.sleep(10)
