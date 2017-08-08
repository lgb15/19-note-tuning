# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 13:55:27 2017

@author: budd
"""

def synthesizer(path):
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
    import nttet_parser as ntp
    import matplotlib.pyplot as plt

    parts=ntp.parts_parse(path)
    instruments=ntp.instrument_parse(path)
    full_notes=ntp.get_notes(path)
    full_durations=ntp.get_durations(path)
    
   
    # maximal amplitude
    MAXAMP = 32767 / 2
    # sampling frequency (in Herz: the number of samples per second)
    SAMPLINGFREQ = 48000
    # the number of channels (1=mono, 2=stereo)
    NCHANNELS = 2
    # filename of output
    filename = path[:-4] + '.wav'
    # initialise mixer module
    pygame.mixer.init(frequency=SAMPLINGFREQ, channels=NCHANNELS)
    
    for n in range(len(parts)):
        print(n)
        instrument=instruments[n]
        durations=full_durations[n]
        notes=full_notes[n]
        # sound length (seconds, a float)
        SOUNDLEN = durations
        # sound frequency (in Herz: the number of vibrations per second)
#        SOUNDFREQ=full_notes[n]
        # chord expressed as a numpy array of ratios
        chord = notes
            
        
        if instrument == 'alto sax':    
            amp = numpy.array([-5,-5.5,-6,-6.9,-7,-7.6,-7.8,-9.1,-8.6,-8.8,-8.5,-9.2,-10.2,-10.7]) #alto sax
        if instrument == 'organ':    
            amp = numpy.array([-6,-7.1,-7.6,-7.4,-9.5,-10.2])  #organ
        if instrument == 'oboe':    
            amp = numpy.array([-6.5,-5,-6.1,-5.9,-7.5,-7.1,-8.1,-9,-8.6,-10.1]) #oboe
        if instrument == 'trumpet':    
            amp = numpy.array([-4.6,-4.8,-5.8,-7,-7.8,-8.4,-9.6,-10.1,-10,-10.8,-11.2,-10.6,-11.1,-11.9,-11.3,-11.4,-11.4]) #trumpet
        overtones = 10**(amp+5)    
    
        if n==0:        
            full_sine=[]
          
        for i in range(len(notes)):
            chord = notes[i]
            CHORDLEN = SOUNDLEN[i]   
#            NOTEFREQ = SOUNDFREQ[i]
            # create a single vibration (range with stepsize = number of samples per cycle)
            t = numpy.arange(CHORDLEN*SAMPLINGFREQ)
            # t is now increasing numbers between 0 and 2 pi. Apply a sinusoid to
            # make them into a wave function
            sine_temp = t*0.0
            for p in chord:
                for m,v in enumerate(overtones):
                    sine_temp += v*numpy.sin(m*p*2*numpy.pi/SAMPLINGFREQ*t)
        
            sine_temp = signal.tukey(len(sine_temp))*sine_temp
        
            if i==0:
                sine = 1*sine_temp
            else:
                sine = numpy.concatenate([sine, sine_temp])
        full_sine.append(sine)
            
    print(len(full_sine[0]),len(full_sine[1]),len(full_sine[2]))
        
    final_sine=0.*full_sine[0]
    for i in range(len(full_sine)):
        final_sine+=full_sine[i]        
        
#        for i in range(len(full_sine)):
#            print(len(full_sine[i]))
#            if i==0:
#                final_sine=full_sine[i]
#            else:
#                final_sine=numpy.add(final_sine,full_sine[i])
        
        
        
        
#     multiply the current numbers by the maximum amplitude to make audible sound
    final_sine *= MAXAMP/max(final_sine)
    
#    plt.subplot(411)    
#    plt.plot(full_sine[0])
#    plt.subplot(412)
#    plt.plot(full_sine[1])
#    plt.subplot(413)
#    plt.plot(full_sine[2])
#    plt.subplot(414)
#    plt.plot(final_sine)
#    plt.show

    # for stereo: double the samples, and reshape the single array to two arrays
    if NCHANNELS == 2:
        final_sine = numpy.repeat(final_sine, 2, axis=0)
        final_sine.reshape(len(final_sine)/2,2)

    # create a sound from the list
    snd = pygame.mixer.Sound(final_sine.astype('int16'))


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

