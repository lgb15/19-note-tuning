# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 09:01:10 2017

@author: budd
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 15:01:03 2017

@author: budd
"""

def chord_sequence(roots, ratios, durations, name):
    ####
    #function to produce a .wav file of a given chord
    #roots = numpy array of chord root notes 
    #ratio = numpy array of ratios to root for subsequent notes
    #duration = duration of chord in Seconds
    ####
    import wave
    import numpy
    import pygame
    from scipy import signal
    # sound length (seconds, a float)
    SOUNDLEN = durations
    # sound frequency (in Herz: the number of vibrations per second)
    SOUNDFREQ = roots
    # chord expressed as a numpy array of ratios
    chord = ratios
    # maximal amplitude
    MAXAMP = 32767 / 2
    # sampling frequency (in Herz: the number of samples per second)
    SAMPLINGFREQ = 48000
    # the number of channels (1=mono, 2=stereo)
    NCHANNELS = 2
    # filename of output
    filename = name + '.wav'    


    # # # # #
    # PREPARE

    # initialise mixer module
    pygame.mixer.init(frequency=SAMPLINGFREQ, channels=NCHANNELS)
      
    for i in range(len(ratios)):    
        chord = ratios[i]
        CHORDLEN = SOUNDLEN[i]   
        NOTEFREQ = SOUNDFREQ[i]
        # create a single vibration (range with stepsize = number of samples per cycle)
        t = numpy.arange(CHORDLEN*SAMPLINGFREQ)
        # t is now increasing numbers between 0 and 2 pi. Apply a sinusoid to
        # make them into a wave function
        sine_temp = t*0.0
        for n in chord:
            sine_temp += numpy.sin(2*n*numpy.pi*NOTEFREQ/SAMPLINGFREQ*t)
        
        sine_temp = signal.tukey(len(sine_temp))*sine_temp        
        
        if i ==0:
            sine = 1*sine_temp
        else:
            sine = numpy.concatenate([sine, sine_temp])
        
    # multiply the current numbers by the maximum amplitude to make audible sound
    sine *= MAXAMP/max(sine)

    # for stereo: double the samples, and reshape the single array to two arrays
    if NCHANNELS == 2:
        sine = numpy.repeat(sine, 2, axis=0)
        sine.reshape(len(sine)/2,2)

    # create a sound from the list
    snd = pygame.mixer.Sound(sine.astype('int16'))


    # # # # #
    # WAVE IT UP
	
    # open new wave file
    sfile = wave.open(filename, 'w')

    # set the parameters
    sfile.setframerate(SAMPLINGFREQ)
    sfile.setnchannels(NCHANNELS)
    sfile.setsampwidth(2)

    # write raw PyGame sound buffer to wave file
    sfile.writeframesraw(snd.get_raw())

    # close file
    sfile.close()

