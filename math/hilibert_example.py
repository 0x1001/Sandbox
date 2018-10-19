import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import hilbert

freq = 13560000
sampling_freq = 135600000

time = [i*1/sampling_freq for i in range(1000)]
sine_wave = [np.sin(2*np.pi*freq*t) for t in time]

side_band_freq = 848000
side_band_sine_wave = [np.sin(2*np.pi*side_band_freq*t) for t in time]

mixed_signal = []
for i in range(len(time)):
    mixed_signal.append(sine_wave[i] * side_band_sine_wave[i])

plt.plot(time, mixed_signal)
plt.show()

hilibert_data = hilbert(mixed_signal)
hilibert_data = np.abs(hilibert_data)

plt.plot(time, mixed_signal)
plt.plot(time, hilibert_data)
plt.show()