from machine import Pin
import utime

in1 = Pin(15,Pin.OUT)
in2 = Pin(14,Pin.OUT)

while True:
    
    
    in1.value(0)
    in2.value(0)
    utime.sleep(1)
    
    
    in1.value(1)
    in2.value(0)
    utime.sleep(1)
    
    in1.value(0)
    in2.value(1)
    utime.sleep(1)
    
    
    
    in1.value(1)
    in2.value(1)
    utime.sleep(1)
    