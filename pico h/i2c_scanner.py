from machine import Pin, I2C  # Importing necessary classes

i2c = I2C(0, sda=Pin(20), scl=Pin(21), freq=400000)  # Your I2C configuration

print('Scanning i2c bus...')
devices = i2c.scan()

if len(devices) == 0:
    print("No i2c device found!")
else:
    print('i2c devices found:', len(devices))

for device in devices:
    print("Decimal address: ", device, " | Hexa address: ", hex(device))
