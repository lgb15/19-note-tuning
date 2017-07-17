# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 11:35:35 2017

@author: budd
"""

import wave

import numpy
import pygame

import matplotlib.pyplot as plt

# # # # #
# 12-note equal temperament #
a12 = 440.0
as12 = bf12 = 466.1637615180899
b12 = cf12 = 493.8833012561241
bs12 = c12 = 523.2511306011972
cs12 = df12 = 554.3652619537442
d12 = 587.3295358348151
ds12 = ef12 = 622.2539674441618
e12 = ff12 = 659.2551138257398
es12 = f12 = 698.4564628660078
fs12 = gf12 = 739.9888454232688
g12 = 783.9908719634985
gs12 = af12 = 830.6093951598903

# 19-note equal temperament #
a19 = 440.0
as19 = 456.3482195563244
bf19 = 473.30385793688026
b19 = 490.8894838150792
bs19 = 509.1285044043967
c19 = 528.0451966143654
cs19 = 547.6647393641703
df19 = 568.0132470968582
d19 = 589.1178045387678
ds19 = 611.0065027504487
ef19 = 633.7084765170539
e19 = 657.2539431279737
es19 = 681.6742425973284
f19 = 707.0018793788565
fs19 = 733.2705656307191
gf19 = 760.515266087813
g19 = 788.7722446013131
gs19 = 818.0791124073976
af19 = 848.4748781893957


def playthisnote(x):
    # CONSTANTS

    # sound length (seconds, a float)
    SOUNDLEN = 3.0
    # sound frequency (in Hertz: the number of vibrations per second)
    SOUNDFREQ = x

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
    
    # calculate the amount of sound cycles in the lenght of this sound
    ncycles = SOUNDLEN * SOUNDFREQ
    # calculate the amount of samples per cycle
    spc = int((SAMPLINGFREQ * SOUNDLEN) / ncycles)
    
    # create a single vibration (range with stepsize = number of samples per cycle)
    sine = numpy.arange(0, 2*numpy.pi, (2*numpy.pi)/spc)
    # sine is now just increasing numbers between 0 and 2 pi. Apply a sinusoid to
    # make them into a wave function
    sine = numpy.sin(sine)
    # multiply the current numbers by the maximum amplitude to make audible sound
    sine *= MAXAMP

    # repeat the single cycle as much as we need to fill the current sound
    sine = numpy.hstack(int(ncycles)*list(sine))
    # for stereo: double the samples, and reshape the single array to two arrays
    if NCHANNELS == 2:
        sine = numpy.repeat(sine, 2, axis=0)
        sine.reshape(len(sine)/2,2)

    # create a sound from the list
    snd = pygame.mixer.Sound(sine.astype('int16'))


    # # # # #
    # WAVE IT UP
	
    # open new wave file
    sfile = wave.open('x.wav', 'w')

    # set the parameters
    sfile.setframerate(SAMPLINGFREQ)
    sfile.setnchannels(NCHANNELS)
    sfile.setsampwidth(2)

    # write raw PyGame sound buffer to wave file
    sfile.writeframesraw(snd.get_buffer().raw)

    # close file
    sfile.close()

    plt.plot(sine[:1000])
    plt.show()
