#!/usr/bin/env python3
# Copyright 2018-Today S Sai Vineet
# BITS Pilani, Goa campus
# Goa cmapus best campus fuk u pilani pussies
import requests

import gi
gi.require_version("Notify", "0.7")
from gi.repository import Notify


Notify.init ("Auto login")
LOGIN_URL = "https://campnet.bits-goa.ac.in:8090/login.xml"
USERNAME = "f20180168"
PASSWORD = "elephant7s"

def show_notification(message):
    notif = Notify.Notification.new ("Auto login script",
                                     message,
                                     "dialog-information")
    notif.show ()

data = {
    "mode": 191,
    "username": USERNAME,
    "password": PASSWORD,
    "a": 123456789,
    "producttype": 0
} 

login = requests.post(LOGIN_URL, data = data)
if ("LIVE" in login.text):
    show_notification("You have been logged in successfully")
elif ("data transfer" in login.text):
    show_notification("Your data transfer has been exceeded")
else:
    show_notification("Something went wrong")
    print (login.text)

