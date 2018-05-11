from time import sleep
from controller_rpi import ask

def send(lora):
    counter = 0
    print("LoRa Sender")

    while True:
        counter = ask()
        payload = 'Glow ({0})'.format(counter)
        print("Sending packet: \n{}\n".format(payload))
        lora.println(payload)
        sleep(5)
        if counter < 0 or counter > 2:
            return 
