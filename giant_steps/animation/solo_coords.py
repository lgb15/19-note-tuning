# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 10:31:22 2017

@author: budd
"""
import numpy as np
import sys
sys.path.insert(0,'/home/ara/budd/19-note-tuning/giant_steps/')
from gscoltrane_solo import *

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

solo_notes=[
cs19,
e19,
gs19,
high_b19,
high_as19,
gs19,
fs19,
ds19,
b19,
low_fs19,
d19,
e19,
fs19,
high_a19,
g19,
d19,
b19,
low_g19,
bf19,
low_af19,
low_g19,
low_f19,
low_ef19,
low_f19,
low_g19,
low_af19,
bf19,
c19,
d19,
f19,
cs19,
as19,
low_gs19,
low_gf19,
e19,
ds19,
cs19,
bs19,
ds19,
gs19,
high_bs19,
ds19,
fs19,
high_a19,
high_cs19,
e19,
fs19,
gs19,
high_b19,
f19,
g19,
high_b19,
high_d19,
high_b19,
high_a19,
g19,
a19,
high_cs19,
high_bs19,
high_b19,
af19,
gf19,
es19,
ef19,
df19,
bs19,
es19,
gs19,
e19,
gf19,
es19,
e19,
gf19,
f19,
df19,
bf19,
low_f19,
low_af19,
low_f19,
low_g19,
e19,
ef19,
df19,
c19,
bf19,
low_af19,
bf19,
c19,
ef19,
e19,
d19,
c19,
b19,
b19,
low_g19,
a19,
b19,
c19,
d19,
e19,
g19,
high_b19,
high_bf19,
high_a19,
af19,
gf19,
gf19,
af19,
gs19,
gf19,
ef19,
es19,
gf19,
gf19,
high_bs19,
high_es19,
high_bs19,
bs19,
bs19,
high_as19,
high_b19,
high_as19,
fs19,   ###first chorus end###
high_c19,
high_cs19,
high_d19,
high_cs19,
high_c19,
high_b19,
d19,
g19,
high_b19,
high_bf19,
high_a19,
af19,
high_c19,
high_bf19,
g19,
f19,
ef19,
g19,
ef19,
ef19,
gs19,
high_bs19,
high_ds19,
high_b19,
gf19,
ds19,
ds19,
ds19,
gs19,
bs19,
ds19,
fs19,
high_a19,
high_cs19,
e19,
fs19,
gs19,
b19,
f19,
g19,
high_a19,
high_b19,
g19,
e19,
d19,
cs19,
c19,
g19,
df19,
ef19,
es19,
df19,
gs19,
fs19,
ds19,
cs19,
bs19,
bs19,
high_as19,
af19,
es19,
es19,
bf19,
bf19,
f19,
af19,
high_c19,
high_bf19,
g19,
f19,
ef19,
f19,
g19,
high_bf19,
af19,
high_bf19,
high_c19,
high_b19,
high_c19,
c19,
high_b19,
g19,
high_a19,
high_b19,
ef19,
f19,
g19,
bf19,
af19,
ef19,
bs19,
af19,
df19,
as19,
af19,
gf19,
bs19,
af19,
af19,
af19,
cs19,
e19,
gs19,
high_b19,
fs19,
gs19,
high_as19,
high_cs19,
high_a19,
high_as19,
high_bf19,
high_b19
]

solo_cumulative = np.cumsum(solo_durations)
