#! /usr/bin/env python3

import subprocess

ret = subprocess.check_output(['vcgencmd', 'measure_temp']).decode('utf8')
_, temp = ret.split('=')
temp = temp[:-3]
print('Die Temperatur der CPU beträgt {} °C'.format(temp))
