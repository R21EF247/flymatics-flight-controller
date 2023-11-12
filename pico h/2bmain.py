import motor_controller
import math
import gyro
import drone_math
import coms
import time
from machine import Pin
time.sleep(10)
led=Pin(25,Pin.OUT)
for i in range(10):
    cdata=coms.coms_data()
    led.toggle()
    time.sleep(0.1)
try:
    while True:
        if(cdata is not None and cdata[5]>50):
            break
        cdata=coms.coms_data()
        gdata=gyro.gyrodata()
        if(cdata is not None):
            drone_math.a.setthrust((cdata[3]/200)+0.5)
        angle=(math.atan(gdata[0]/(gdata[1]+0.000001)))
        powr=((gdata[0]**2+gdata[1]**2)**(0.5))
        #drone_math.a.moveDirection(angle+(3.1415926535/2),powr)
        motor_controller.pwmGenerate(motor_controller.duty(0,indv=drone_math.a.rpms))
        pass
    
except KeyboardInterrupt:
    motor_controller.pwmGenerate(motor_controller.duty(-2))
motor_controller.pwmGenerate(motor_controller.duty(-2))

    
    
    
    
    
    
    
    