import gc
print("file")
gc.collect()
print(gc.mem_free())
f = open('base64.txt', 'r')
content = f.read() 
f.close()

POST_URL = "https://speech.googleapis.com/v1/speech:recognize/?key=AIzaSyDvqe4gC1kSlsn4k_2nJzWtZORk2HfXgeU"

json_data = {
    "config":{
    "encoding": "AMR",
    "languageCode":"en-US",
    "sampleRateHertz": 8000,
    "audioChannelCount": 1,
    "enableSeparateRecognitionPerChannel": False,
},
"audio":{
    "content": content
}
  
}
del content

gc.collect()
print(gc.mem_free())
import time
import board
print("board")
gc.collect()
print(gc.mem_free())
import busio
print("busio")
gc.collect()
print(gc.mem_free())
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
print("socket")
gc.collect()
print(gc.mem_free())
from adafruit_esp32spi import adafruit_esp32spi
print("espspi")
gc.collect()
print(gc.mem_free())
import adafruit_requests as requests 
print("requests")
gc.collect()
print(gc.mem_free())

from digitalio import DigitalInOut
print("dio")
gc.collect()
print(gc.mem_free())

import busio 
print("busio")


gc.collect()
print(gc.mem_free())
#import speechtotext
print("speachtotext")

gc.collect()
print(gc.mem_free())

try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise
 
# If you are using a board with pre-defined ESP32 Pins:
esp32_cs = DigitalInOut(board.ESP_CS)
esp32_ready = DigitalInOut(board.ESP_BUSY)
esp32_reset = DigitalInOut(board.ESP_RESET)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset, debug=1)

print("Connecting to AP...")
while not esp.is_connected:
    try:
        esp.connect_AP(secrets["ssid"], secrets["password"])
    except RuntimeError as e:
        print("could not connect to AP, retrying: ", e)
        continue
print("Connected to", str(esp.ssid, "utf-8"), "\tRSSI:", esp.rssi)

# Initialize a requests object with a socket and esp32spi interface 
socket.set_interface(esp)
requests.set_socket(socket, esp)
print("Firmware vers.", esp.firmware_version)
print(adafruit_esp32spi.__version__)
print("RSSI:   ", esp.rssi)
print("SSID:    ", str(esp.ssid, 'utf-8'))
print("BSSID:    {5:02X}:{4:02X}:{3:02X}:{2:02X}:{1:02X}:{0:02X}".format(*esp.bssid))
print("IP:      ", esp.pretty_ip(esp.ip_address))
print("Netmask:  %d.%d.%d.%d" % (esp.network_data['netmask'][0], esp.network_data['netmask'][1], esp.network_data['netmask'][2], esp.network_data['netmask'][3]))
print("Gateway:  %d.%d.%d.%d" % (esp.network_data['gateway'][0], esp.network_data['gateway'][1], esp.network_data['gateway'][2], esp.network_data['gateway'][3]))
print("LAN ping: %dms" % esp.ping(esp.network_data['gateway']))
print("WAN ping: %dms" % esp.ping("1.1.1.1"))

TEXT_URL = "http://wifitest.adafruit.com/testwifi/index.html"
JSON_GET_URL = "https://httpbin.org/get"
JSON_POST_URL = "https://httpbin.org/post"



time.sleep(5)
gc.collect()
print(gc.mem_free()) 
response = requests.post(POST_URL, json = json_data)

json_resp = response.json()

print("JSON Data received from server:", json_resp)
print('-'*40)
response.close()
# speechtotext.Call_Speech_to_Text(requests)



  
