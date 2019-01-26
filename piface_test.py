from time import sleep
import pifacedigitalio as p

p.init()
while(True):
    p.digital_write(0,1) # Ausgang 1 einschalten
    sleep(1)
    p.digital_write(0,0) # Ausgang 1 ausschalten
    sleep(1) 
