from machine import Pin, PWM, UART
import machine
import utime

pwm = PWM(Pin(15))
pwm.duty_u16(5000*65535) 
uart = UART(1, 9600)
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

def set_pin(pin,value):
    pins[pin].duty_u16(int(value*65535/254))
    
def set_pin_off(pin,value):
    pins[pin].duty_u16(int(value*65535/254))


while True:
    data = uart.read(1)
    if data :
        data = data.decode() 
        print(data)
        #play_audio(6000)
        #for color, pin in pins.items():
        value = data
        if value == b'0':
            set_pin_off("blue",0)
            set_pin_off("green",0)
            set_pin_off("red",0)
            play_audio(6000)
        elif value == b'1':
            set_pin("blue",122)
            set_pin_off("green",0)
            set_pin_off("red",0)
            play_audio(6000)
        elif value == b'2':
            set_pin("green",122)
            set_pin_off("blue",0)
            set_pin_off("red",0)
            play_audio(6000)
        elif value == b'3':
            set_pin("red",122)
            set_pin_off("blue",0)
            set_pin_off("green",0)
            play_audio(6000)
        #play_audio(6000)
        
