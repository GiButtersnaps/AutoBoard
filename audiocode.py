import time
import board
import digitalio
from audiocore import WaveFile

try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        pass  # not always supported by every board!


wave_file = open("StreetChicken.wav", "rb")
wave = WaveFile(wave_file)
audio = AudioOut(board.A0)

#while True:
#    audio.play(wave)

    # This allows you to do other things while the audio plays!
#        t = time.monotonic()
#        while time.monotonic() - t < 6:
#            pass

#    audio.pause()
#    print("Waiting for button press to continue!")
#    while button.value:
#        pass
#    audio.resume()
#    while audio.playing:
#        pass
#    print("Done!")

def playaudio(waveFile):
    if waveFile == 'invalid command':
        wave_file = open("InputCommand.wav", "rb")
    elif waveFile == 'move complete':
        wave_file = open("MoveComplete.wav", "rb")
    wave = WaveFile(wave_file)
    audio = AudioOut(board.A0)
    audio.play(wave)
    while audio.playing:
        pass


#########  KEV Code of dev
import board
import busio
import usb_cdc
import time
import supervisor
import digitalio
import usb_cdc
Button = digitalio.DigitalInOut(board.D13)
Button.direction = digitalio.Direction.INPUT
last_write = time.monotonic()

# supervisor.disable_autoreload()
while True:

    if usb_cdc.data.in_waiting:
        print("waiting")
        msg = usb_cdc.data.readline()
        if msg:
            print("recieved:", msg)
            usb_cdc.data.write(msg)
    # now = time.monotonic()
    # if now - last_write > 5:
    #     last_write = now
    #     usb_cdc.data.write(b"hello world\n")
    if (Button.value == True):
        usb_cdc.data.write(b"1\n")
    #if supervisor.runtime.serial_bytes_available:
      #  value = input()
    # value = usb_cdc.data.readline()
    # usb_cdc.data.write(value)
    time.sleep(0.5)
