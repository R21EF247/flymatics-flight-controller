import motor_controller
import gyro
import coms
import drone_math
while True:
    data=get_data()
    status=data["status"]
    power=data["power"]
    angle=data["angle"]
    a.setthrust(power)
    a.setDirection(angle)
    
    
    
    