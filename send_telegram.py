#!/usr/bin/env python3.8
import re
import sys
from html import escape
from time import sleep

import requests


def alert_on_telegram(msg: str):
    """
    This function will send an alert to telegram notifying about the change
    If BOT_TOKEN is not provided, this function will not run
    :param msg: The message
    :return: None
    """
    CHAT_ID = "YOUR CHAT ID"
    BOT_TOKEN = "YOUR BOT TOKEN"
    if BOT_TOKEN and CHAT_ID:
        try_again = True
        while try_again:
            try:
                x = requests.get(
                    "https://api.telegram.org/bot"
                    + BOT_TOKEN
                    + "/sendMessage?chat_id="
                    + str(CHAT_ID)
                    + "&parse_mode=MarkdownV2"
                    "&text=" + msg[:1000]
                )
                x.raise_for_status()
                try_again = False
            except requests.exceptions.ConnectionError:
                try_again = True
                print("Connection error, retrying in 5 seconds...")
                sleep(5)


def parse_time(message: str):
    def recursive_format(second: int):
        time: str
        if second < 60:
            time = f"{second} seconds"
        elif 60 < second < 3600:
            minutes, second = divmod(second, 60)
            time = f"{minutes}min {second}s"
        else:
            hours, second = divmod(second, 3600)
            time = f"{hours} hr " + recursive_format(second)
        return time

    output: str
    parse_re = re.compile(r".+:.+ (\d+) seconds")

    try:
        seconds = int(parse_re.findall(message)[0])
        output = recursive_format(seconds)
    except ValueError:
        output = "Something went wrong processing seconds." \
                 "\n \"" + message + "\""

    return output


if __name__ == '__main__':
    message = input()
    if len(message) <= 1:
        print("ERROR! did not receive any input", file=sys.stderr)
        sys.exit(1)
    time_seconds = parse_time(message)
    message = f"`{message[:33]} + {parse_time(message)}`" \
              f"\n\nIf the outage duration is less than 5 minutes, ignore this message\." \
              f" \\%23Outage"

    alert_on_telegram(message)
