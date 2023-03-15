import RPi.GPIO as GPIO
def decimal2binary(value): 
    return [int(bit) for bit in bin(value % 256)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

for x in dac:
    GPIO.setup(x, GPIO.OUT)

try:
    while(1):
        a = (input("Введите число от 0 до 255\n"))
        if (a == "q"): 
            break
        print("значение в вольтах: {:.3f}".format(3.3 * abs(int(a)) / 255))
        out = decimal2binary(abs(int(a)))
        for x in range(8):
            GPIO.output(dac[x], out[x])   

except ValueError:
    print("ошибка: введено не число")
    
finally:
    for x in dac:
        GPIO.output(x, 0)
    GPIO.cleanup()
    