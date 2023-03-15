import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

p = GPIO.PWM(22, 1000)

try:
    
    
    while(1): 
        a = (input("Введите коэфицент заполнения\n"))
        if (a == "q"):
            break
        p.start(abs(float(a))%101)
        print("значение в вольтах: {:.3f}".format(3.3 * (abs(float(a))%101) / 100))

except ValueError:
    print("ошибка: введено не число")
    
finally:
    p.stop()
    GPIO.cleanup()
    
