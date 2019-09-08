# -*- coding: utf-8 -*-

"""The extension helps you to show and set charge thresholds for Huawei Matebook 13/14/X Pro."""

import os
import subprocess

from albertv0 import *

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Huawei WMI charge thresholds"
__version__ = "1.0"
__trigger__ = "hw"
__author__ = "Jason Lin <jasonosfc@163.com>"
__dependencies__ = []
__fname__ = "/sys/devices/platform/huawei-wmi/charge_thresholds"

iconPath = iconLookup("preferences-system")

def handleQuery(query):
    if not query.isTriggered:
        return None

    with open(__fname__,'r',encoding='utf-8') as f:
        lines=f.readlines()
        first_line=lines[0]
        currentChargeThresholds=first_line.split()

    items = []
    if currentChargeThresholds:
        items.append(Item(
            id = __prettyname__,
            icon = iconPath,
            text = "Current charge thresholds: LOW %s; HIGH: %s" % (currentChargeThresholds[0],currentChargeThresholds[1]),
        ))
    items.append(Item(
        id = __prettyname__,
        icon = iconPath,
        text = "Siwtch to Home Mode: LOW 40; HIGH: 70",
        actions = [
            FuncAction(
                "Set New Charge Thresholds",
                lambda: setNewThresholds("40", "70")
                ),
            ]
    ))
    items.append(Item(
        id = __prettyname__,
        icon = iconPath,
        text = "Switch to Office Mode: LOW 70; HIGH: 90",
        actions = [
            FuncAction(
                "Set New Charge Thresholds",
                lambda: setNewThresholds("70", "90")
                ),
            ]
    ))
    items.append(Item(
        id = __prettyname__,
        icon = iconPath,
        text = "Switch to Travel Mode: LOW 90; HIGH: 99",
        actions = [
            FuncAction(
                "Set New Charge Thresholds",
                lambda: setNewThresholds("90", "99")
                ),
            ]
    ))

    return items

def setNewThresholds(lower, upper):
    command = "echo '%s %s' > %s" % (lower,upper,__fname__)
    proc = subprocess.Popen(command, shell=True)
    proc = subprocess.Popen("notify-send 'Charge thresholds already set to %s - %s'" % (lower, upper), shell=True)
