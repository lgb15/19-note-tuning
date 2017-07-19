# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 15:25:38 2017

@author: budd
"""

from freqs_and_rats import *

#==============================================================================
# ttet_just_equiv = [1,16/15,10/9,6/5,5/4,4/3,45/32,3/2,8/5,5/3,9/5,15/8]
# ttet_badness = []
# 
# for i in ttet_ratios:
#     v = ttet_ratios.index(i)
#     diff = abs(i - ttet_just_equiv[v])
#     ttet_badness.append(diff)
#     
# ntet_just_equiv = [1,25/24,16/15,10/9,75/64,6/5,5/4,32/25,4/3,45/32,64/45,3/2,36/25,8/5,5/3,128/75,9/5,15/8,48/25]
# ntet_badness = []
# 
# for i in ntet_ratios:
#     v = ntet_ratios.index(i)
#     diff = abs(i - ntet_just_equiv[v])
#     ntet_badness.append(diff)
#==============================================================================

def badness(chord, et):        
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
    




