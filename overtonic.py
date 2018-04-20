# overtonic.py
# Using Fast Fourier Transforms (FFTs) to determine an instrument based on the musical overtones of its sound

import numpy as np
from scipy.fftpack import fft
from scipy.io import wavfile as wav
from pylab import *
import matplotlib.pyplot as plt
import peakutils.plot

##################################################

# Program variables

# The sound file you want to read from
# If you change this, remember to change the savefig location to match your directory tree!
soundfile = 'sound/sine-a4.wav'

# Set to True if you want the output figure (with peaks) to save!
# Usually best to leave at false except for demos, etc.
# Split is a bit questionable, figure out how to do it the right way
# This will need to be changed if a different directory tree is used
savefig = False
savefigloc = 'images/' + soundfile.split('/')[1] + '.png'


##################################################

# Print helpful data
print("Reading from", soundfile)
frate, data = wav.read(soundfile)
print("FRATE:", frate)
print("DATA:", data)

length = len(data)
nUniquePts = int(ceil((length+1)/2.0))
fft = (abs(fft(data)[0:nUniquePts]) / float(length))**2 

if length % 2 > 0: # odd, double the fft set
   fft[1:len(fft)] = fft[1:len(fft)] * 2
else: # even, double the fft set except for Nyquist
   fft[1:len(fft) -1] = fft[1:len(fft) - 1] * 2 

array = arange(0, nUniquePts, 1.0) * (frate / length)
x = array[:4000] # cap output to 4000 Hz

y = (10*log10(fft))[:4000] # cap output to 4000 Hz

y2 = y + np.polyval([0.002,-0.08,5], x)
base = peakutils.baseline(y2, 2) # remove the baseline for a cleaner reading

# TODO: Conditional-ize the thres and min_dist per sound if possible
indexes = peakutils.indexes(y, thres=0.7, min_dist=100)

print("Indexes", indexes)
print("array of Indexes", array[indexes])

peakutils.plot.plot(x, y2-base, indexes) # plot x and y with removed baseline, peaks (indexes)
plt.title('Peaks after Removed Baseline')
xlabel('Frequency (Hz)')
ylabel('Amplitude (dB) without Baseline')

# Save figure, use for demo only
if savefig == True:
    plt.savefig(savefigloc, bbox_inches='tight')

plt.show()

# TODO:
	# Set the conditions for the if/else block
    # Add a "more or less" part to ensure that this works with other files of the same sound source

inst = None
if len(indexes) == 1: # Sine waves have one peak
    inst = 'a SINE WAVE'
elif len(indexes) == 2: # Whistles have two peaks
    inst = 'a WHISTLE'
elif len(indexes) == 5: # Pianos have five peaks, but not really and this should be changed! (TODO)
    inst = 'a PIANO'

if inst:
    print('It looks like the sound you gave me is', inst)
else:
    print("Aww, the sound you gave me is unsure or not supported")
print()