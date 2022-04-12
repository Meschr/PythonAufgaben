# import modules and give them abbreviations (for scipy just import fft)
import numpy as np
from scipy.fft import fft
import pandas as pd
import matplotlib.pyplot as mpl
# set number of samples, sample frequency and sample time
k = 1000
fs = 1000
ts = 1/fs
# use numpy to create array of time samples and sinus signal
x = np.linspace(0,ts*k,k)
y = np.sin(100*2*np.pi*x) + 0.5*np.sin(180*2*np.pi*x)
# use scipy to get fft and power spectrum as pandas time series
spec = fft(y)
freq = np.linspace(0,fs/2,k//2)
power = pd.Series(2/k*np.abs(spec[0:k//2]),freq)
# use matplotlib to create figure and 1st subplot to plot numpy arrays
mpl.figure()
mpl.subplot(3,1,1)
mpl.title('Composed Sinus Signal')
mpl.xlabel('Time')
mpl.ylabel('Signal')
mpl.plot(x,y)
# create 2nd subplot and plot power spectrum from pandas series
mpl.subplot(3,1,3)
mpl.title('Power Spectrum of Signal')
mpl.xlabel('Frequency')
mpl.ylabel('Power')
mpl.plot(power)
# show figure on screen. This will block the execution until figure is closed
mpl.show()