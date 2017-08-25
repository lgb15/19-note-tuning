# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 15:25:38 2017

@author: budd
"""

from freqs_and_rats import *

def badness(chord, et):
#==============================================================================
#     returns the badness of a single chord as a fraction between 0 and 1
#       chord = array of note ratios in chord
#       et = equal temperament regime, 12 or 19
#==============================================================================
    values = []    
    for i in chord:
        if et == 12:
            v = ttet_ratios.index(i)
        if et == 19:
            v = ntet_ratios.index(i)
        values.append(v)
    badness = []
    for j in values:
        if et == 12:
            k = ttet_diff[j]
        if et == 19:
            k = ntet_diff[j]   
        badness.append(k)
    total_badness = sum(badness)/len(chord)
    return(total_badness)
    
def sequence_badness(chords, et):  
#==============================================================================
#     returns the average badness of a chord sequence as a fraction between 0 and 1
#       chords = list of arrays of note ratios in chords
#       et = equal temperament regime, 12 or 19
#==============================================================================      
    chord_badness = []
    for i in range(len(chords)):
        chord = chords[i]
        cb = badness(chord,et)
        chord_badness.append(cb)
    total_badness = sum(chord_badness)/len(chords)
    return(total_badness)
    




