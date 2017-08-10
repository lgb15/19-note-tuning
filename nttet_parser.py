# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 13:40:17 2017

@author: budd
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 10:52:38 2017

@author: budd
"""
from ntfreqs import *   
import numpy as np

def parts_parse(path):   
    f=open(path,'r')        
    for line in f:
        if '@parts:' in line:
            p = line
            parts=int(p[7])
    return parts

def instrument_parse(path):
    f=open(path,'r')
    instruments=[]
    for line in f:
        if '@instrument' in line:
            i = line
            part = int(line[11])
            part-=1
            instruments.insert(part,i[13:-1])
    return instruments

def notes_parse(path):
    f=open(path,'r')
    notes=[]
    for j in range(parts_parse(path)):
        notes.append([])
    for line in f:
        if '@notes' in line:
            part=int(line[6])
            l=line.partition(':')[2]
            while '\n' in l:
                l=l.replace('\n','')
            l=eval(l)
            notes[part-1].extend(l)
    return notes

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
    n_d=notes_parse(path)
    durations=[]
    f=open(path,'r')
    for line in f:
        if '@bpm:' in line:
            while '\n' in line:
                line=line.replace('\n','')
            bpm=float(line[5:])
    for i in range(len(n_d)):
        durations_temp=[]
        for j in range(len(n_d[i])):         
            if len(n_d[i][j])==2:
                d=n_d[i][j][1]    
            durations_temp.append(d)
        durations.append(durations_temp)
    for i in range(len(durations)):
        durations[i]=[j*4*(60/bpm) for j in durations[i]]
    return durations
    
def dynamic_parse(path):
    f=open(path,'r')
    volumes=[]
    for line in f:
        if '@volume' in line:
            while '\n' in line:
                line=line.replace('\n','')
            part=int(line[7])
            volume=float(line[9:])
            volumes.insert(part,volume)
    return volumes