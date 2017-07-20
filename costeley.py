# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 11:50:47 2017

@author: budd
"""

from freqs_and_rats import *

roots = [
fs19,
fs19,
fs19,
fs19,
gs19,
a19,
a19,
a19,
b19,
cs19,
cs19,
cs19,
cs19,
fs19,
fs19,
fs19,
fs19,
b19,
b19,
a19,
a19,
d19,
d19,
cs19,
cs19,
a19,
fs19,
cs19,
cs19,
cs19,
d19,
d19,
b19,
b19,
cs19,
cs19,
cs19,
cs19,
fs19,
fs19,
b19,
b19,
cs19,
cs19,
fs19,
fs19,
cs19,
e19,
e19,
fs19,
fs19,
fs19,
gs19,
gs19,
gs19,
gs19,
gs19,
cs19,
cs19,
cs19,
cs19,
fs19,
fs19,
fs19,
fs19,
fs19,
cs19,
cs19,
cs19,
cs19,
es19,
b19,
a19,
gs19,
gs19,
gs19,
cs19,
cs19,
a19,
a19,
fs19,
fs19,
fs19,
b19,
b19,
a19,
b19,
b19,
fs19,
fs19,
fs19,
fs19,
]

ratios = (
[0.5*ntet_ratios[0],0.5*ntet_ratios[11],ntet_ratios[0]],
[0.5*ntet_ratios[0],ntet_ratios[0]],
[0.5*ntet_ratios[0],ntet_ratios[3]],
[0.5*ntet_ratios[0],0.5*ntet_ratios[11],ntet_ratios[5]],
[0.5*ntet_ratios[0],0.5*ntet_ratios[8],ntet_ratios[2]],
[ntet_ratios[0],ntet_ratios[6],2*ntet_ratios[0]],
[ntet_ratios[0],ntet_ratios[9],2*ntet_ratios[3]],
[ntet_ratios[0],ntet_ratios[11],2*ntet_ratios[6]],
[ntet_ratios[0],ntet_ratios[8],2*ntet_ratios[3]],
[ntet_ratios[0],ntet_ratios[6],2*ntet_ratios[0]],
[ntet_ratios[0],ntet_ratios[8],2*ntet_ratios[0]],
[ntet_ratios[0],ntet_ratios[8],ntet_ratios[11]],
[ntet_ratios[0],ntet_ratios[6],ntet_ratios[11]],
[ntet_ratios[0],ntet_ratios[11]],
[ntet_ratios[0],ntet_ratios[11]],
[0.5*ntet_ratios[0],ntet_ratios[0],ntet_ratios[5]],
[0.5*ntet_ratios[0],ntet_ratios[0],ntet_ratios[5]],
[ntet_ratios[0],ntet_ratios[11],2*ntet_ratios[5]],
[ntet_ratios[0],ntet_ratios[11],2*ntet_ratios[5]],
[ntet_ratios[0],2*ntet_ratios[6]],
[ntet_ratios[0],ntet_ratios[6],2*ntet_ratios[6]],
[ntet_ratios[0],ntet_ratios[6]],
[ntet_ratios[0],ntet_ratios[6]],
[ntet_ratios[0],ntet_ratios[5],2*ntet_ratios[0]],
[ntet_ratios[0],ntet_ratios[5],2*ntet_ratios[0]],
[2*ntet_ratios[0],2*ntet_ratios[6]],
[0.5*ntet_ratios[0],ntet_ratios[5],ntet_ratios[11]],
[ntet_ratios[0],ntet_ratios[11],2*ntet_ratios[0]],
[ntet_ratios[0],ntet_ratios[13]],
[ntet_ratios[0],ntet_ratios[13],ntet_ratios[16]],
[ntet_ratios[0],ntet_ratios[11]],
[ntet_ratios[0],ntet_ratios[6],ntet_ratios[11]],
[ntet_ratios[0],ntet_ratios[11],2*ntet_ratios[0]],
[ntet_ratios[0],ntet_ratios[14],2*ntet_ratios[0]],
[ntet_ratios[0],ntet_ratios[11]],
[ntet_ratios[0],ntet_ratios[8],ntet_ratios[11]],
[ntet_ratios[0],ntet_ratios[8]],
[ntet_ratios[0],ntet_ratios[6],ntet_ratios[11]],
[ntet_ratios[0],ntet_ratios[5]],
[0.5*ntet_ratios[0],ntet_ratios[0],ntet_ratios[5]],
[ntet_ratios[0],ntet_ratios[11]],
[ntet_ratios[0],ntet_ratios[6],2*ntet_ratios[0]],
[ntet_ratios[0],ntet_ratios[6],ntet_ratios[11]],
[ntet_ratios[0],ntet_ratios[6],ntet_ratios[11]],
[0.5*ntet_ratios[0],ntet_ratios[0]],
[0.5*ntet_ratios[0],ntet_ratios[0],ntet_ratios[5]],
[ntet_ratios[0],ntet_ratios[11]],
[0.5*ntet_ratios[0],ntet_ratios[6]],
[0.5*ntet_ratios[0],ntet_ratios[0],ntet_ratios[6]],
[0.5*ntet_ratios[0],0.5*ntet_ratios[14],ntet_ratios[0]],
[0.5*ntet_ratios[0],0.5*ntet_ratios[11]],
[0.5*ntet_ratios[0],0.5*ntet_ratios[11],0.5*ntet_ratios[16]],
[0.5*ntet_ratios[0],0.5*ntet_ratios[8],0.5*ntet_ratios[11]],
[0.5*ntet_ratios[0],0.5*ntet_ratios[6],0.5*ntet_ratios[11]],
[0.5*ntet_ratios[0],0.5*ntet_ratios[3],0.5*ntet_ratios[11]],
[0.5*ntet_ratios[0],0.5*ntet_ratios[6]],
[0.5*ntet_ratios[0],0.5*ntet_ratios[6],ntet_ratios[0]],
[0.5*ntet_ratios[0],ntet_ratios[0],ntet_ratios[11]],
[0.5*ntet_ratios[0],ntet_ratios[0],ntet_ratios[11]],
[0.5*ntet_ratios[0],ntet_ratios[0],2*ntet_ratios[0]],
[0.5*ntet_ratios[0],ntet_ratios[0],2*ntet_ratios[0]],
[ntet_ratios[0],ntet_ratios[11]],
[0.5*ntet_ratios[0],ntet_ratios[0]],
[0.5*ntet_ratios[0],ntet_ratios[8]],
[0.5*ntet_ratios[0],ntet_ratios[5]],
[0.5*ntet_ratios[0],ntet_ratios[0],0.5*ntet_ratios[5]],
[ntet_ratios[0],ntet_ratios[8],ntet_ratios[11]],
[ntet_ratios[0],ntet_ratios[6],ntet_ratios[11]],
[ntet_ratios[0],ntet_ratios[3],ntet_ratios[11]],
[ntet_ratios[0],ntet_ratios[6],ntet_ratios[11]],
[ntet_ratios[0],ntet_ratios[5]],
[ntet_ratios[0],ntet_ratios[9],ntet_ratios[14]],
[ntet_ratios[0],ntet_ratios[6],2*ntet_ratios[0]],
[0.5*ntet_ratios[0],0.5*ntet_ratios[11],ntet_ratios[6]],
[0.5*ntet_ratios[0],ntet_ratios[6]],
[0.5*ntet_ratios[0],ntet_ratios[0],ntet_ratios[6]],
[ntet_ratios[0],ntet_ratios[11]],
[ntet_ratios[0],ntet_ratios[5],2*ntet_ratios[0]],
[ntet_ratios[0],ntet_ratios[11],2*ntet_ratios[6]],
[ntet_ratios[0],ntet_ratios[6],2*ntet_ratios[0]],
[0.5*ntet_ratios[0],0.5*ntet_ratios[11],ntet_ratios[5]],
[0.5*ntet_ratios[0],ntet_ratios[0],ntet_ratios[5]],
[0.5*ntet_ratios[0],0.5*ntet_ratios[16],0.5*ntet_ratios[5]],
[ntet_ratios[0],ntet_ratios[6],2*ntet_ratios[0]],
[ntet_ratios[0],ntet_ratios[3],2*ntet_ratios[0]],
[ntet_ratios[0],ntet_ratios[11],2*ntet_ratios[6]],
[ntet_ratios[0],ntet_ratios[5],2*ntet_ratios[3]],
[ntet_ratios[0],ntet_ratios[5],2*ntet_ratios[0]],
[0.5*ntet_ratios[0],0.5*ntet_ratios[11],ntet_ratios[8]],
[0.5*ntet_ratios[0],0.5*ntet_ratios[11],ntet_ratios[6]],
[0.5*ntet_ratios[0],0.5*ntet_ratios[11],ntet_ratios[3]],
[0.5*ntet_ratios[0],0.5*ntet_ratios[11],ntet_ratios[6]]
)

durations = (
2.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
0.5,
0.5,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
2.0,
1.0,
1.0,
1.0,
0.5,
0.5,
1.0,
0.5,
0.5,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
0.5,
0.5,
1.0,
1.0,
1.0,
0.5,
0.5,
1.0,
0.5,
0.5,
2.0,
2.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
1.0,
0.5,
0.5,
1.0,
1.0,
1.0,
0.5,
0.5,
0.5,
0.5,
1.0,
1.0,
2.0
)