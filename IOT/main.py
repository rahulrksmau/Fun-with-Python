from gpiozero import LED, LEDBoard
import sx127x
import config_lora
from RPi import GPIO
#import leds

import LoRaReceiver
# import LoRaReceiverCallback

def main():
    controller = config_lora.Controller()
    lora = controller.add_transceiver(sx127x.SX127x(name = 'LoRa'),
                                      pin_id_ss = config_lora.Controller.PIN_ID_FOR_LORA_SS,
                                      pin_id_RxDone = config_lora.Controller.PIN_ID_FOR_LORA_DIO0)
    print('lora', lora)
    LoRaReceiver.receive(lora)
    # LoRaReceiverCallback.receiveCallback(lora)

if __name__ == '__main__':
    print ("Green -> 0\nRed -> 1\nYellow -> 2")
    main()
    try:
        GPIO.cleanup()
    except Exception as e:
        print(e)
    print ("Cleaning Led pins")
    # leds.clean()
    
