# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 13:08:48 2017

@author: budd
"""

import wave

import numpy
import pygame

import matplotlib.pyplot as plt


# # # # #
# CONSTANTS

# sound length (seconds, a float)
SOUNDLEN = 1.0
# sound frequency (in Herz: the number of vibrations per second)
SOUNDFREQ = [440,550,660]

# maximal amplitude
MAXAMP = 32767 / 2
# sampling frequency (in Herz: the number of samples per second)
SAMPLINGFREQ = 48000
# the number of channels (1=mono, 2=stereo)
NCHANNELS = 2


# # # # #
# PREPARE

# initialise mixer module
pygame.mixer.init(frequency=SAMPLINGFREQ, channels=NCHANNELS)

# initialise sine waves
sine = []
sine = numpy.asarray(sine)

# add different frequency waves
spc= []
# add different frequency waves
for i in SOUNDFREQ:
    # calculate the amount of sound cycles in the lenght of this sound
    ncycles = SOUNDLEN * i
    # calculate the amount of samples per cycle
    spc_i = int((SAMPLINGFREQ * SOUNDLEN) / ncycles)
    spc.append(spc_i)
    for j in spc:
        # create a single vibration (range with stepsize = number of samples per cycle)
        sine_temp = numpy.arange(0, 2*numpy.pi, (2*numpy.pi)/j)
        # sine is now just increasing numbers between 0 and 2 pi. Apply a sinusoid to
        # make them into a wave function
        sine = numpy.sin(sine_temp)
        # multiply the current numbers by the maximum amplitude to make audible sound
        sine_temp *= MAXAMP/2

        # repeat the single cycle as much as we need to fill the current sound
        sine = numpy.hstack(int(ncycles)*list(sine))
        # for stereo: double the samples, and reshape the single array to two arrays
        if NCHANNELS == 2:
            sine_temp = numpy.repeat(sine_temp, 2, axis=0)
            sine_temp.reshape(len(sine_temp)/2,2)
    
        sine = numpy.concatenate((sine, sine_temp), axis=0)

        # create a sound from the list
        snd = pygame.mixer.Sound(sine.astype('int16'))

sine = sine.reshape(len(sine)/2,2)

#plt.plot(sine[:1000])
#plt.show()

# # # # #
# WAVE IT UP
	
# open new wave file
sfile = wave.open('pure_tone.wav', 'w')

# set the parameters
sfile.setframerate(SAMPLINGFREQ)
sfile.setnchannels(NCHANNELS)
sfile.setsampwidth(2)

# write raw PyGame sound buffer to wave file
sfile.writeframesraw(snd.get_buffer().raw)

# close file
sfile.close()