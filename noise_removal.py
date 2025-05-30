#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Audio signal processing
from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq, ifft
import sys
np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(suppress=False)

# converter audio.mp3 para audio.wav
"""
from pydub import AudioSegment
sound = AudioSegment.from_mp3("audio.mp3")
sound.export("audio.wav", format="wav")
"""

def AudioSignalProcessing(audio):

    
    # Import the .wav format audio into two variables: 
    # sampling (int)
    # audio signal (numpy array)
    
    sampling, signal = read(audio)
    
    print(*repr(np.array(signal)))
    
    # time duration of the audio
    length = signal.shape[0] / sampling

    # x axis based on the time duration
    time = np.linspace(0., length, signal.shape[0])
    
    # show original signal
    plt.plot(time, signal)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Original signal")
    plt.show()

    
    # apply Fourier transform and normalize
    transform = fft(signal)
    
    # obtain frequencies
    xf = fftfreq(transform.size, 1/sampling) 
    
    # show transformed signal (frequencies domain)
    plt.plot(xf, abs(transform)/np.linalg.norm(transform))
    plt.xlabel("Frecuency (Hz)")
    plt.ylabel("Amplitude")
    plt.title("Frequency domain signal")
    plt.show()

    
    # filter the transformed signal to a 40% of its maximum amplitude
    threshold = np.amax(transform)*0.4
    filtered = np.copy(transform)
    filtered[abs(transform) < 0.4 * max(abs(transform))] = 0
    
    # show filtered transformed signal
    plt.plot(xf,abs(filtered)/np.linalg.norm(filtered))
    plt.xlabel("Frecuency (Hz)")
    plt.ylabel("Amplitude")
    plt.title("FILTERED time domain signal")
    plt.show()
    
    
    # transform the signal back to the time domain
    filtered = ifft(filtered)
    
    # show original signal filtered
    plt.plot(time, filtered)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Filtered signal")
    plt.show()
    
    
    # convert audio signal to .wav format audio
    # write(audio.replace(".wav", " filtrado.wav"), sampling, filtrada.astype(signal.dtype))
    
    return None

AudioSignalProcessing("audio.wav")


# In[12]:





# In[ ]:




