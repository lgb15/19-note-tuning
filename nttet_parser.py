# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 10:52:38 2017

@author: budd
"""
from ntfreqs import *   
import numpy as np

def instrument_parse(path):
    f=open(path,'r')
    instruments=[]
    for line in f:
        if '@instrument:' in line:
            i = line
            instruments.append(i[12:-1])
    return instruments

def parts_parse(path):   
    f=open(path,'r')        
    parts=[]
    for line in f:
        if '@part:' in line:
            p = line
            parts.append(int(p[6]))
    return parts
 
def notes_parse(path):
    f=open(path,'r')          
    notes=[]
    for line in f:
        if '@notes:' in line:
            l=line.partition(':')[2]
            while '\n' in l:
                l=l.replace('\n','')
            l=eval(l) 
            notes.append(l)
    n_d = np.array(notes)
    return(n_d)

def get_notes(path):
    n_d=notes_parse(path)
    notes=[]
    for i in range(len(n_d)):
        notes_temp=[]
        for j in range(len(n_d[i])):
            notes_temp.append(n_d[i][j][0])
        notes.append(notes_temp)
    return notes
    
def get_durations(path):
    global d
    n_d=notes_parse(path)
    durations=[]
    for i in range(len(n_d)):
        durations_temp=[]
        for j in range(len(n_d[i])):         
            if len(n_d[i][j])==2:
                d=n_d[i][j][1]    
            durations_temp.append(d)
        durations.append(durations_temp)
    return durations
    
            
            
    