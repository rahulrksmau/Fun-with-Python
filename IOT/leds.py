from gpiozero import LED, LEDBoard
import time

board = LEDBoard(red=2,green=4,yellow=3)

def glow(led_light, sec=2):
    print (led_light.pin)
    led_light.on()
    time.sleep(sec)
    led_light.off()


def ask():
    n = int(input('LED index = '))
    if n >=0 and n <=2:
        glow(board[n])
    else:
        print ("No Led")
    return n


def clean():
    for led in board:
        led.off()


