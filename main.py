#!/usr/bin/env python3
# Copyright 2018-Today S Sai Vineet
# BITS Pilani, Goa campus
# Goa cmapus best campus fuk u pilani pussies
import requests
import config

import gi
gi.require_version("Notify", "0.7")
from gi.repository import Notify

from enum import Enum


Notify.init ("Auto login")
LOGIN_URL = "https://campnet.bits-goa.ac.in:8090/login.xml"
USERNAME = config.USERNAME
PASSWORD = config.PASSWORD


TrialEnum = Enum("TrialResponse", "SUCCESS DATA_EXCEEDED ERROR")


def show_notification(message):
    notif = Notify.Notification.new ("Auto login script",
                                     message,
                                     "dialog-information")
    notif.show ()


def try_login(username, password):
    data = {
        "mode": 191,
        "username": username,
        "password": password,
        "a": 123456789,
        "producttype": 0
    } 

    login = requests.post(LOGIN_URL, data = data)
    if ("LIVE" in login.text):
        return TrialEnum.SUCCESS
    elif ("data transfer" in login.text):
        return TrialEnum.DATA_EXCEEDED
    else:
        return TrialEnum.ERROR


if __name__ == '__main__':
    attempt = None
    for i, (username, password) in enumerate(zip(USERNAME, PASSWORD)):
        attempt = try_login(username, password)
        if attempt is TrialEnum.SUCCESS:
            # Finally post a notification
            show_notification(f"Auto login succeeded on try {i+1}")
            break
    else:
        if attempt is TrialEnum.DATA_EXCEEDED:
            show_notification("Data exceeded in all IDs")
        else:
            show_notification("Something went wrong...")

