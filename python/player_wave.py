import pyaudio
import wave  

chunk = 1


f = wave.open(r"samples\EpicScifi_Mini_SP\ButtonFX_03_554.wav","rb")

p = pyaudio.PyAudio()  

print("Sample width: {0}".format(f.getsampwidth()))
print("Channels width: {0}".format(f.getnchannels()))


stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),
                rate = f.getframerate(),  
                output = True)  

data = f.readframes(chunk)  


while data:
    #print(len(data))
    ch1 = int.from_bytes(data[:3], "little", signed=True)
    ch2 = int.from_bytes(data[3:], "little", signed=True)

    ch1 = int(ch1 * 1)
    ch2 = int(ch2 * 1)

    data = ch1.to_bytes(3, "little", signed=True) + ch2.to_bytes(3, "little", signed=True)
    #print(int.from_bytes(data[:2], "little"))
    stream.write(data)
    data = f.readframes(chunk)  


stream.stop_stream()  
stream.close()  

p.terminate()