# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 15:01:03 2017

@author: budd
"""

def chord(root, ratio, duration, name, plot='n'): #inversion='root'):
    ####
    #function to produce a .wav file of a given chord
    #root = root note of chord in Hertz
    #ratio = numpy array of ratios to root for subsequent notes
    #duration = duration of chord in Seconds
    #name = name of saved .wav file
    #plot -- if ='y', returns 
    ####
    import wave
    import numpy
    import pygame
    import matplotlib.pyplot as plt
    # sound length (seconds, a float)
    if type(duration) != float:
        print("Duration must be a float")
    else:
        SOUNDLEN = duration
    # sound frequency (in Herz: the number of vibrations per second)
    SOUNDFREQ = root
    # chord expressed as a numpy array of ratios
    chord = ratio    
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

    # create a single vibration (range with stepsize = number of samples per cycle)
    t = numpy.arange(SOUNDLEN*SAMPLINGFREQ)
    # t is now just increasing numbers between 0 and 2 pi. Apply a sinusoid to
    # make them into a wave function
    sine = 0*t
    for n in chord:
        sine += numpy.sin(2*n*numpy.pi*SOUNDFREQ/SAMPLINGFREQ*t)
        # multiply the current numbers by the maximum amplitude to make audible sound
    sine *= MAXAMP/10
    
    if plot == 'y':
        time=t/SAMPLINGFREQ
        normal_amp = sine/max(abs(sine))        
        freq = numpy.fft.rfft(normal_amp,SAMPLINGFREQ)
        peak = numpy.argmax(freq)
        print(peak)
        
        plt.figure(1)
        plt.subplot(211)
        plt.plot(time[:4800000],normal_amp[:480000])
        plt.xlabel('Time(s)')                
        
        plt.subplot(212) 
        plt.semilogy(abs(freq[:2000]))
        plt.show
        
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

