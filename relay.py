#!/usr/bin/env python

# https://github.com/pimoroni/explorer-hat/blob/master/examples/test.py

# https://github.com/pimoroni/explorer-hat/blob/master/documentation/Technical-reference.md

import time
import explorerhat


def ohai(channel, event):
    touched[channel - 1] = True
    print("{}: {}".format(channel, event))

explorerhat.output[0].on()
explorerhat.output[3].on()


while True:
    print(explorerhat.input.read())

    explorerhat.output.toggle()

    time.sleep(100.0/1000.0)

explorerhat.pause()