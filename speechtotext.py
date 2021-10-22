import board
import base64
import busio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_esp32spi import adafruit_esp32spi
# import adafruit_esp32spi.adafruit_esp32spi_requests as requests
import secrets


# google_application_credentials = "autoboard-329721-3464793b915b.json"
# audio = audioio.AudioOut(board.A0)
 # audiofiles = ["rimshot.wav", "laugh.wav", ]



#PA27 51 microphone
#PA24 45    left audio
#PA25  46   right audio

##this file will initialize the esp32s connection to the network 
# then be incharge of sending rest api requests to 
# the api and recieving them
# network data held in secerets
# call post with base64 encoded audio data
# recieve the data in the response

# esp32_cs = DigitalInOut(board.ESP_CS)
# esp32_ready = DigitalInOut(board.ESP_BUSY)
# esp32_reset = DigitalInOut(board.ESP_RESET)
# spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
# esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)


# if esp.status == adafruit_esp32spi.WL_IDLE_STATUS:
#     print("ESP32 found and in idle mode")
#     print("Firmware vers.", esp.firmware_version)
#     print("MAC addr:", [hex(i) for i in esp.MAC_address])




def Call_Speech_to_Text(requests):

    audiofile = "apitestaudio.wav"
    encoded = "base64.txt"
    #encoded = base64.b64encode(audiofile)

    #POST_URL = "https://speech.googleapis.com/v1/speech:recognize" + secrets['key']
 
    POST_URL = "https://speech.googleapis.com/v1/speech:recognize:AIzaSyDvqe4gC1kSlsn4k_2nJzWtZORk2HfXgeU"

    json_data = {
        "config":{
        "languageCode":"en-US",
        "sampleRateHertz": 46000,
        "enableTimeWordOffsets": False,
            "audioChannelCount": 4,
        "enableSeparateRecognitionPerChannel": False,
    },
    "audio":{
        "content": encoded
    }

    }

    response = requests.post(POST_URL, json = json_data)

    #json_response = response.json()

    json_resp = response.json()
    # Parse out the 'json' key from json_resp dict.
    print("JSON Data received from server:", json_resp['json'])
    print('-'*40)
    response.close()








