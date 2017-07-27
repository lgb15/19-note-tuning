# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:17:25 2017

@author: budd
"""

from gs_chords import *
import numpy as np

low_cs19 = [35.6,180]
low_df19 = [35.6,70]
low_d19 = [78,300]
low_ds19 = [121.4,180]
low_ef19 =[121.4,70]
low_e19 = [170,300]
low_es19 = [218,120]
low_f19 = [265,300]
low_fs19 = [314,180]
low_gf19 = [314,70]
low_g19 = [360,300]
low_gs19 = [408,180] 
low_af19 = [408,70]
a19 = [448,300]
as19 = [492,180]
bf19 = [492,70]
b19 = [530,300]
bs19 = [582,120]
c19 = [626,300]
cs19 = [675,180]
df19 = [675,70]
d19 = [714,300]
ds19 = [763,180]
ef19 =[763,70]
e19 = [805,300]
es19 = [853,120]
f19 = [896,300]
fs19 = [952,180]
gf19 = [952,70]
g19 = [996,300]
gs19 = [1045,180]
af19 = [1045,70]
high_a19 = [1083,300]
high_as19 = [1130,180]
high_bf19 = [1130,70]
high_b19 = [1163,300]
high_bs19 = [1218,120]
high_c19 = [1260,300]
high_cs19 = [1310,180]
high_df19 = [1310,70]
high_d19 = [1350,300]
high_ds19 = [1440,180]
high_ef19 = [1440,70]
high_e19 = [1440,300]
high_es19 = [1490,120]

chord_list=[
[b19,low_fs19,as19,ds19],
[d19,low_fs19,a19,c19],
[low_g19,low_fs19,b19,d19],
[bf19,low_f19,low_af19,d19],
[ef19,low_g19,bf19,df19],
[ef19,low_g19,bf19,df19],
[ef19,low_g19,bf19,df19],
[ef19,low_g19,bf19,df19],
[ef19,low_g19,bf19,df19],
[as19,cs19,es19,gs19],
[as19,cs19,es19,gs19],
[as19,cs19,es19,gs19],
[ds19,low_gf19,as19,cs19],
[low_gs19,bs19,ds19,gf19],
[b19,low_fs19,a19,ds19],
[e19,low_gs19,b19,ds19],
[low_g19,b19,d19,f19],
[c19,low_e19,low_g19,b19],
[c19,low_e19,low_g19,b19],
[c19,low_e19,low_g19,b19],
[c19,low_e19,low_g19,b19],
[c19,low_e19,low_g19,b19],
[gf19,as19,df19,es19],
[gf19,as19,df19,es19],
[gf19,as19,df19,es19],
[bs19,low_gf19,bf19,ef19],
[low_es19,low_gf19,bs19,ef19],
[low_es19,low_gf19,bs19,ef19],
[bf19,low_af19,df19,f19],
[bf19,low_af19,df19,f19],
[bf19,low_af19,df19,f19],
[ef19,low_g19,bf19,df19],
[low_af19,c19,ef19,g19],
[low_af19,c19,ef19,g19],
[d19,low_f19,a19,c19],
[d19,low_f19,a19,c19],
[low_g19,d19,f19],
[low_g19,b19,d19,f19],
[c19,low_g19,b19,e19],
[c19,low_g19,b19,e19],
[gf19,as19,df19,es19],
[gf19,as19,df19,es19],
[bs19,ef19,gf19,as19],
[bs19,ef19,gf19,as19],
[es19,bs19,ef19,af19],
[es19,bs19,ef19,af19],
[cs19,low_gs19,b19,e19],
[low_fs19,as19,cs19,e19]
]

chord_cumulative=np.cumsum(chord_durations)