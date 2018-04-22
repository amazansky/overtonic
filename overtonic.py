# overtonic.py (v1.0.0)
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

soundfilename = soundfile.split('/')[1] # Don't touch

# Set to True if you want the output figure (with peaks) to save!
# Usually best to leave at false except for demos, etc.
# Split is a bit questionable, figure out how to do it the right way
# This will need to be changed if a different directory tree is used
savefig = False
savefigloc = 'images/' + soundfilename + '.png'

# Set to True if you want the output figure (with peaks) to be displayed
# in a matplotlib window!
showfig = True

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
y3 = y2-base

# TODO: Conditional-ize the thres and min_dist per sound if possible
indexes = peakutils.indexes(y, thres=0.7, min_dist=100)

y4 = y3[indexes]

print("Indexes", indexes)
print("array of Indexes", array[indexes])
print("y of Indexes (amplitude for array of indexes)", y4) # amplitude

peakutils.plot.plot(x, y3, indexes) # plot x and y with removed baseline, peaks (indexes)
plt.title('Peaks after Removed Baseline: ' + soundfilename)
xlabel('Frequency (Hz)')
ylabel('Amplitude (dB) without Baseline')

# Save figure, use for demo only (see program variables)
if savefig == True:
    plt.savefig(savefigloc, bbox_inches='tight')
# Show figure, best to leave on (see program variables)
if showfig == True:
    plt.show()

# TODO (future) - make this whole if/else thing into a neural network so long conditionals don't need to be a thing
    
inst = None
if len(indexes) == 1: # Sine waves have one peak
    inst = 'a SINE WAVE'
elif len(indexes) == 2: # Whistles have two peaks
    inst = 'a WHISTLE'
elif len(indexes) == 5 and round(y4[0] / y4[1], 2) == 1.24 and round(y4[0] / y4[2], 2) == 1.38 and round(y4[0] / y4[3], 2) == 1.24: # it's sketchy but it works
    inst = 'a PIANO'

if inst:
    print('It looks like the sound you gave me is', inst)
else:
    print("Aww, the sound you gave me is unsure or not supported")
print()