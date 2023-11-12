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
        frequency = 50
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
        r=[]
        for i in indv:
            a1=(i*(8-7))+7
            r.append(int(a1 * 65025 / 100))
        print(r)
        return(r)
    while True:
        try:
            value=f
            r=[]
            a1=(value*(8-7))+7
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