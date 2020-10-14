#!/usr/bin/python
#
# Monitor removal of bluetooth reciever
# set .bashrc to call this script on boot up
import os
import sys
import subprocess
import time

def blue_it():
    status = subprocess.call('ls /dev/input/event0 2>/dev/null', shell=True)
    while status == 0:
        print("Bluetooth UP")
        print(status)
        time.sleep(15)
        status = subprocess.call('ls /dev/input/event0 2>/dev/null', shell=True)
    else:
        waiting()

def waiting():
    subprocess.call('killall -9 pulseaudio', shell=True)
    time.sleep(3)
    subprocess.call('pulseaudio --start', shell=True)
    subprocess.call('pactl -- set-sink-volume 0 70%', shell=True)
    time.sleep(2)
    status = subprocess.call('ls /dev/input/event0 2>/dev/null', shell=True)  
    while status == 2:
        print("Bluetooth DOWN")
        print(status)
        subprocess.call('~/beerOclock/autopair', shell=True)
        time.sleep(15)
        status = subprocess.call('ls /dev/input/event0 2>/dev/null', shell=True)
    else:
        blue_it() 

blue_it()
