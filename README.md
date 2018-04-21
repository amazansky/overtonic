# Overtonic
Overtonic is a project that aims to use Fast Fourier Transforms (FFTs) to determine the source of a sound based on its overtones. (Science Fair 2018) :musical_note:

[![Release](https://img.shields.io/github/release/RobotXLabs/overtonic/all.svg?style=for-the-badge)](https://github.com/RobotXLabs/overtonic/releases)

```
computer:overtonic user$ python3 overtonic.py
Reading from sound/sine-a4.wav
FRATE Variable: 11025
DATA Variable: [    0  7940 15384 ... 31997 30888 27848]
Indexes [1596]
FreqArray of Indexes [439.8975]
It looks like the sound you gave me is a SINE WAVE
```

## Dependencies
1. NumPy
1. SciPy
   1. scipy.fftpack
   1. scipy.io
1. PyLab
1. MatPlotLib
   1. matplotlib.pyplot
1. PeakUtils

## Acknowledgements
* FFT Identification code: [Basic Sound Processing with Python](http://samcarcagno.altervista.org/blog/basic-sound-processing-python/) _(Sam Carcagno, 2013) **Modified to acommodate frequency and amplitude**_
* PeakUtils: [PeakUtils tutorial (docs)](https://peakutils.readthedocs.io/en/latest/tutorial_a.html)
* With help from [thatoddmailbox](https://github.com/thatoddmailbox/)