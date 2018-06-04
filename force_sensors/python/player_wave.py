import pyaudio
import wave  
import serial
import common
import threading

CHUNK = 256


class Volume:
    def __init__(self):
        self._volume = 0
        self._lock = threading.RLock()
        threading.Thread(target=self._volume_control).start()

    def set_volume(self, v):
        with self._lock:
            self._volume = v

    def get_volume(self):
        with self._lock:
            return self._volume

    def _volume_control(self):
        ser = serial.Serial("COM34", 9600)
        common.wait_for_start(ser)

        while True:
            line = ser.readline()

            if common.first_button(line):
                potentiometer = common.get_value(line)
                if 0 < potentiometer < 200:
                    self.set_volume(0)
                elif 200 < potentiometer < 400:
                    self.set_volume(0.1)
                elif 400 < potentiometer < 700:
                    self.set_volume(0.25)
                elif 700 < potentiometer < 1024:
                    self.set_volume(1)


def play():
    f = wave.open(r"samples\EpicScifi_Mini_SP\ButtonFX_03_554.wav","rb")
    p = pyaudio.PyAudio()

    print("Sample width: {0}".format(f.getsampwidth()))
    print("Channels width: {0}".format(f.getnchannels()))

    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels=f.getnchannels(),
                    rate=f.getframerate(),
                    output=True)

    vol = Volume()
    while True:
        data = f.readframes(CHUNK)

        if not data:
            f.rewind()
            data = f.readframes(CHUNK)

        modified_data = b''
        volume = vol.get_volume()
        for i in range(0, len(data), 6):
            ch1 = int.from_bytes(data[i:i+3], "little", signed=True)
            ch2 = int.from_bytes(data[i+3:i+6], "little", signed=True)

            ch1 = int(ch1 * volume)
            ch2 = int(ch2 * volume)

            modified_data = modified_data + ch1.to_bytes(3, "little", signed=True) + ch2.to_bytes(3, "little", signed=True)

        stream.write(modified_data)

    stream.stop_stream()
    stream.close()
    p.terminate()


if __name__ == "__main__":
    play()