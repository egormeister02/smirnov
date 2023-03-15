import RPi.GPIO as GPIO
import time 
def decimal2binary(value): 
    return [int(bit) for bit in bin(value % 256)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

for x in dac:
    GPIO.setup(x, GPIO.OUT)

try:
    a = (input("Введите период в секундах\n"))
    while(1): 
        for x in range(256):
            out = decimal2binary(x)
            for i in range(8):
                GPIO.output(dac[i], out[i])   
            print("значение в вольтах: {:.3f}".format(3.3 * x / 255))
            time.sleep(abs(int(a)) / 256)
        for x in range(256):
            out = decimal2binary(255-x)
            for i in range(8):
                GPIO.output(dac[i], out[i])   
            print("значение в вольтах: {:.3f}".format(3.3 * (255-x) / 255))
            time.sleep(abs(int(a)) / 256)

except ValueError:
    print("ошибка: введено не число")
    
finally:
    for x in dac:
        GPIO.output(x, 0)
    GPIO.cleanup()
    