#! /usr/bin/env python3

import subprocess

with open('/sys/class/thermal/thermal_zone0/temp','rb') as f:
    ret = f.read()
temp = int(ret) / 1000
print('Die Temperatur der GPU beträgt {} °C'.format(temp))
