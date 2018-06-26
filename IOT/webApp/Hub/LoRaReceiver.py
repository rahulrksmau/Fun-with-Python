def receive(lora):
    print("LoRa Receiver")

    while True:        
        if lora.receivedPacket():            
            lora.blink_led()
                    
            try:
            	payload = lora.read_payload()
            	print("*** Received message ***\n{0}\n{1}".format(payload.decode(),type(payload)))
	    except Exception as e:
	    	print(e)
	    print("with RSSI: {}\n".format(lora.packetRssi()))
