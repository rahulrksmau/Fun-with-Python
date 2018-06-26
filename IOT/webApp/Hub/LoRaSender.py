from time import sleep
from .controller_rpi import board,glow,off
# leds=['Green','Red','Yellow']
led_status = ['green','red','yellow']
# [1,0,1] red,yellow,green

def send(lora, status):
    print("LoRa Sender")
    status = [status[0]]+status[1:3]
    payload = '{}'.format('-'.join(map(str,status)))
    print("Sending packet: \n{}\n".format(payload))
    lora.println(payload)
    for index in range(len(status)):
        print (index, status[index], board[index])
        if status[index]:
            glow(board[index])
        else:
            off(board[index])
