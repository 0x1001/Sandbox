import pyaudio
import wave  

chunk = 1024


f = wave.open(r"samples\EpicScifi_Mini_SP\ButtonFX_03_554.wav","rb")

p = pyaudio.PyAudio()  

print("Sample width: {0}".format(f.getsampwidth()))
print("Channels width: {0}".format(f.getnchannels()))


stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),
                rate = f.getframerate(),  
                output = True)

while True:
    data = f.readframes(chunk)

    if not data:
        #break
        f.rewind()
        data = f.readframes(chunk)

    modified_data = b''
    for i in range(0, len(data), 6):
        ch1 = int.from_bytes(data[i:i+3], "little", signed=True)
        ch2 = int.from_bytes(data[i+3:i+6], "little", signed=True)

        ch1 = int(ch1 * 1)
        ch2 = int(ch2 * 1)

        modified_data = modified_data + ch1.to_bytes(3, "little", signed=True) + ch2.to_bytes(3, "little", signed=True)

    stream.write(modified_data)

stream.stop_stream()  
stream.close()  

p.terminate()