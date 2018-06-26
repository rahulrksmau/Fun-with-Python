from gpiozero import LED, LEDBoard
from . import sx127x
from . import config_lora
from RPi import GPIO
from . import LoRaSender
# import LoRaDuplex
# import LoRaDuplexCallback

def main(status):
    controller = config_lora.Controller()
    lora = controller.add_transceiver(sx127x.SX127x(name = 'LoRa'),
                                      pin_id_ss = config_lora.Controller.PIN_ID_FOR_LORA_SS,
                                      pin_id_RxDone = config_lora.Controller.PIN_ID_FOR_LORA_DIO0)
    print('lora', lora)
    LoRaSender.send(lora,status)
    
    # LoRaDuplex.duplex(lora)
    # LoRaDuplexCallback.duplexCallback(lora)

if __name__ == '__main__':
    print ("Green -> 0\nRed -> 1\nYellow -> 2")
    led_status = list(map(int,input().split('-')))
    main(led_status)
    try:
        GPIO.cleanup()
    except Exception as e:
        print(e)
    print ("Cleaning Led pins")
    GPIO.setmode(GPIO.BOARD)
    
