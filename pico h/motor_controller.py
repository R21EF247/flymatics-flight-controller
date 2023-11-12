from machine import Pin, PWM
import time
frequency = 0
duty_cycle = 0

# Pin declarat 0)ions
pwmPin = Pin(3)
pwmPin2 = Pin(7)
pwmPin3 = Pin(11)
pwmPin4 = Pin(15)
"""pwmPin5 = Pin('''enter the pin number''')
PwmPin6 = Pin('''enter the pin number''')"""
pwmOutputs = [PWM(i) for i in [pwmPin,pwmPin2,pwmPin3,pwmPin4]]
while True:
    try:
        for i in range(4):
            pwmOutputs[i].duty_u16(0)
        frequency = 70
        if frequency >= 0:
            for i in range(4):
                pwmOutputs[i].freq(int(frequency))
            break
        else:
            print("Frequency cannot be negative. Enter again.")
    except ValueError:
        print("Please enter a valid number.") 
# Function for asking duhh_cycle input
def duty(f,indv=None):
    if(indv!=None):
        a1=int(4815-100+(indv[0]*2677))
        a2=int(4844-100+(indv[1]*2677))
        a3=int(4818-100+(indv[2]*2677))
        a4=int(4830-100+(indv[3]*2677))
        r=[a1,a2,a3,a4]
        print(r)
        return(r)
    while True:
        try:
            value=f
            r=[]
            a1=(value*(10-7))+7
            r=[int(a1 * 65025 / 100) for i in range(6)]
            print(r)
            return(r)
        except ValueError:
            print("Please enter a valid percentage.")
def dutyoff():
    pwmGenerate([0,0,0,0])

def pwmGenerate(duty_cycle):
    for i in range(4):
        pwmOutputs[i].duty_u16(duty_cycle[i])

