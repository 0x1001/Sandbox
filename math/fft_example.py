import numpy as np
from matplotlib import pyplot as plt

freq = 13560000
sampling_freq = 135600000

time = [i*1/sampling_freq for i in range(1000)]
sine_wave = [np.sin(2*np.pi*freq*t) for t in time]

plt.plot(time, sine_wave)
plt.show()

fft_sine = np.fft.fft(sine_wave)
fft_sine = np.abs(fft_sine)

dfreq = sampling_freq/len(sine_wave)
freq_range = [dfreq*i for i in range(int(len(sine_wave)))]

# plot only first part of spectrum
plt.plot(freq_range[:int(len(fft_sine)/2)], fft_sine[:int(len(fft_sine)/2)])
plt.show()