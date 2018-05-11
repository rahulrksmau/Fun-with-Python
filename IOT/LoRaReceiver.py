from controller_rpi import glow, board

def receive(lora):
    print("LoRa Receiver")

    while True:        
        if lora.receivedPacket():            
            lora.blink_led()
                    
            try:
                payload = lora.read_payload()
                payload = payload.decode()
                print("*** Received message ***\n{}".format(payload))
                index = payload.replace('(','#').replace(')','').split('#')[-1].strip()
                leds =  glow(board[index])
            except Exception as e:
                print(e)
            print("with RSSI: {}\n".format(lora.packetRssi()))
            
