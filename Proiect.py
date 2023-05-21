from machine import Pin, PWM, UART
import machine
import utime

pwm = PWM(Pin(15))
pwm.duty_u16(5000*65535) 
uart = UART(0, 9600)
led = Pin(25, Pin.OUT)

pins = {
    'red': PWM(Pin(14)),
    'blue': PWM(Pin(12)),
    'green': PWM(Pin(13))
}

def play_audio(freq):
    pwm.freq(freq)
    pwm.duty_u16(int(0.5 * 65535))
    utime.sleep(0.5)
    pwm.duty_u16(0)
    utime.sleep(0.5)

def set_pin(pin, value):
    pin.duty_u16(int(value*65535/255))

while True:
    while uart.any() > 0:
        uart.read()  
    if uart.any() > 0:
        data = uart.read().decode()
        print(data)
        play_audio(6000)
        for color, pin in pins.items():
            value = int(data.split(f"{color}:")[1].split('|')[0])
            print(pin)
            print(value)
            set_pin(pin, value)
