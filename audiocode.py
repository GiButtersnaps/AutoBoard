import pyaudio
import wave
import requests
import base64
import serial
import time
import RPi.GPIO as GPIO
from pygame import mixer

def play_audio(file_num):
    mixer.init()
    if file_num == -1:
        sound = mixer.Sound('input.wav')
    elif file_num == 0:
        sound = mixer.Sound('completed.wav')
    elif file_num == 1:
        sound = mixer.Sound('one.wav')
    elif file_num == 2:
        sound = mixer.Sound('two.wav')
    elif file_num == 3:
        sound = mixer.Sound('three.wav')
    elif file_num == 4:
        sound = mixer.Sound('four.wav')
    elif file_num == 5:
        sound = mixer.Sound('five.wav')
    else:
        sound = mixer.Sound('six.wav')
    sound.play()
    time.sleep(3)
    


#hopefully this will be an easy way to record the audio
def get_command():
    form_1 = pyaudio.paInt16 # 16-bit resolution
    chans = 1 # 1 channel
    samp_rate = 48000 # 44.1kHz sampling rate
    chunk = 4096 # 2^12 samples for buffer
    record_secs = 7 # seconds to record
    dev_index = 3 # device index found by p.get_device_info_by_index(ii) is either index 1 0r 2
    wav_output_filename = 'command1.wav' # name of .wav file

    audio = pyaudio.PyAudio() # create pyaudio instantiation
    
    
    # set up led
    LED_PIN = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    
# create pyaudio stream
    stream = audio.open(format = form_1,rate = samp_rate,channels = chans,
                    input_device_index = dev_index,input = True,
                    frames_per_buffer=chunk)
    print("recording")
    GPIO.output(LED_PIN, GPIO.HIGH)
    frames = []

# loop through stream and append audio chunks to frame array
    for ii in range(0,int((samp_rate/chunk)*record_secs)):
        data = stream.read(chunk)
        frames.append(data)

    print("finished recording")
    GPIO.output(LED_PIN, GPIO.LOW)

# stop the stream, close it, and terminate the pyaudio instantiation
    stream.stop_stream()
    stream.close()
    audio.terminate()

# save the audio frames as .wav file
    wavefile = wave.open(wav_output_filename,'wb')
    wavefile.setnchannels(chans)
    wavefile.setsampwidth(audio.get_sample_size(form_1))
    wavefile.setframerate(samp_rate)
    wavefile.writeframes(b''.join(frames))
    wavefile.close()

#convert file to amr

    f = open('command1.wav', 'rb')
    file_input = f.read()
    enc = base64.b64encode(file_input)
    f.close()
    POST_URL = "https://speech.googleapis.com/v1/speech:recognize/?key=AIzaSyDvqe4gC1kSlsn4k_2nJzWtZORk2HfXgeU"

    json_data = {
        "config":{
        "encoding": "LINEAR16",
        "languageCode":"en-US",
        "sampleRateHertz": 48000,
        "audioChannelCount": 1,
        "enableSeparateRecognitionPerChannel": False,
        "speechContexts":[
            {
                "phrases":
         [  "move piece location to location", "undo move", "start game", "spin the wheel", "MOVE PIECE 5 spots forwared",
            "move piece 5 spots forward", "MOVE WHITE H8 TO G7", "MOVE BLACK D4 TO E5", "MOVE BLACK D4 TO F6",
            'MOVE', 'WHITE', 'BLACK', 'UNDO', 'START', 'GAME', 'SPIN', 'THE', 'WHEEL', 'BOY', 'GIRL', 'SPOTS', 'FORWARD', 'TO',
            'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8',  
            'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 
            'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 
            'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8'],
                "boost":15 

                }]
    },
    "audio":{
        "content": enc
    },
    
    }
  
    response = requests.post(POST_URL, json = json_data)

    json_resp = response.json()

    print("JSON Data received from server:", json_resp['results'][0]["alternatives"][0]["transcript"])
        
    print('-'*40)
    response.close()

    GPIO.cleanup()
    return json_resp['results'][0]["alternatives"][0]["transcript"]



if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM1', 9600)
    ser.reset_input_buffer()
    play_audio(-1)
    while True:
        line = ser.readline()
        print(line.decode('utf-8').strip())
        if line == b'400\n':
            print(line)
            command = get_command()
            command = command.upper()
            print("pi says")
            print(command)
            
            command = command + "\n"
            ser.write(command.encode('utf-8'))
            print(command.encode('utf-8'))
            time.sleep(1)
        elif line == b'-1\n':
            play_audio(-1)
        elif line == b'0\n':
            play_audio(0)
        elif line == b'1\n':
            play_audio(1)
        elif line == b'2\n':
            play_audio(2)
        elif line == b'3\n':
            play_audio(3)
        elif line == b'4\n':
            play_audio(4)
        elif line == b'5\n':
            play_audio(5)
        elif line == b'6\n':
            play_audio(6)
