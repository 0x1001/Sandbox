import pyaudio
import wave  
import serial
import common
import threading
import queue

CHUNK = 32


class Volume:
    def __init__(self):
        self._volume_1 = 0
        self._volume_2 = 0
        self._lock = threading.RLock()
        threading.Thread(target=self._volume_control).start()

    def set_volume_1(self, v):
        with self._lock:
            self._volume_1 = v

    def set_volume_2(self, v):
        with self._lock:
            self._volume_2 = v

    def get_volume_1(self):
        with self._lock:
            return self._volume_1

    def get_volume_2(self):
        with self._lock:
            return self._volume_2

    def _volume_control(self):
        ser = serial.Serial("COM3", 9600)
        common.wait_for_start(ser)

        while True:
            line = ser.readline()

            if common.first_button(line):
                potentiometer = common.get_value(line)
                #volume = self._calculate_volume_1(potentiometer)
                volume = self._calculate_volume_2_alt(potentiometer)
                self.set_volume_1(volume)

            elif common.second_button(line):
                potentiometer = common.get_value(line)
                #volume = self._calculate_volume_2(potentiometer)
                volume = self._calculate_volume_2_alt(potentiometer)
                self.set_volume_2(volume)

    def _calculate_volume_1(self, potentiometer):
        if 0 < potentiometer <= 700:
            volume = 0
        elif 700 < potentiometer <= 800:
            volume = 0.1
        elif 800 < potentiometer <= 900:
            volume = 0.5
        elif 900 < potentiometer <= 1024:
            volume = 1
        else:
            volume = 0

        return volume

    def _calculate_volume_2(self, potentiometer):
        if 0 < potentiometer <= 500:
            volume = 0
        elif 500 < potentiometer <= 600:
            volume = 0.1
        elif 600 < potentiometer <= 700:
            volume = 0.5
        elif 700 < potentiometer <= 1024:
            volume = 1
        else:
            volume = 0

        return volume

    def _calculate_volume_1_alt(self, potentiometer):
        RANGE_MAX = 1
        RANGE_MIN = 0.1

        if potentiometer < 800:
            return 0.0

        return (potentiometer - 800) * (RANGE_MAX - RANGE_MIN) / (1023.0 - 800) + RANGE_MIN

    def _calculate_volume_2_alt(self, potentiometer):
        RANGE_MAX = 1
        RANGE_MIN = 0.1

        if potentiometer < 400:
            return 0.0

        return (potentiometer - 400) * (RANGE_MAX - RANGE_MIN) / (1023.0 - 400) + RANGE_MIN


def play():
    data_queue = queue.Queue(maxsize=1)
    file_1 = wave.open(r"samples\051-d#.wav","rb")
    file_2 = wave.open(r"samples\048-c.wav", "rb")
    p = pyaudio.PyAudio()

    print("Sample width 1: {0}".format(file_1.getsampwidth()))
    print("Channels width 1: {0}".format(file_1.getnchannels()))

    print("Sample width 2: {0}".format(file_2.getsampwidth()))
    print("Channels width 2: {0}".format(file_2.getnchannels()))

    if file_1.getsampwidth() != file_2.getsampwidth() or file_1.getnchannels() != file_2.getnchannels():
        raise Exception("Sample size or number of channels does not match!")

    stream = p.open(format=p.get_format_from_width(file_1.getsampwidth()),
                    channels=file_1.getnchannels(),
                    rate=file_1.getframerate(),
                    output=True)

    threading.Thread(target=_write_stream, args=(stream, data_queue)).start()

    vol = Volume()
    while True:
        data_1 = file_1.readframes(CHUNK)
        data_2 = file_2.readframes(CHUNK)

        if not data_1:
            file_1.rewind()
            file_1.setpos(4096)
            data_1 = file_1.readframes(CHUNK)

        if not data_2:
            file_2.rewind()
            file_2.setpos(4096)
            data_2 = file_2.readframes(CHUNK)

        output = b''
        volume_1 = vol.get_volume_1()
        volume_2 = vol.get_volume_2()
        for i in range(0, len(data_1), 6):
            # First sample
            s1_ch1 = int.from_bytes(data_1[i:i+3], "little", signed=True)
            s1_ch2 = int.from_bytes(data_1[i+3:i+6], "little", signed=True)

            s1_ch1 = int(s1_ch1 * volume_1)
            s1_ch2 = int(s1_ch2 * volume_1)

            # Second sample
            s2_ch1 = int.from_bytes(data_2[i:i+3], "little", signed=True)
            s2_ch2 = int.from_bytes(data_2[i+3:i+6], "little", signed=True)

            s2_ch1 = int(s2_ch1 * volume_2)
            s2_ch2 = int(s2_ch2 * volume_2)

            # Combined sound:
            ch1 = int((s1_ch1 + s2_ch1) / 2)
            ch2 = int((s1_ch2 + s2_ch2) / 2)

            output = output + ch1.to_bytes(3, "little", signed=True) + ch2.to_bytes(3, "little", signed=True)

        data_queue.put(output)

    stream.stop_stream()
    stream.close()
    p.terminate()


def _write_stream(stream, queue_data):
    while True:
        data = queue_data.get()
        stream.write(data)

if __name__ == "__main__":
    play()
