from freqs_and_rats import *
from chord_sequence_new import chord_sequence

m7 = [ntet_ratios[k] for k in (0,6,11,15)]
a6 = [ntet_ratios[k] for k in (0,8,16)]
sc = [ntet_ratios[k] for k in (0,8,14)]
chord_sequence((c19,c19,c19),(m7,a6,sc),(3.,3.,3.),'example19')

m7 = [ttet_ratios[k] for k in (0,4,7,10)]
a6 = [ttet_ratios[k] for k in (0,5,10)]
sc = [ttet_ratios[k] for k in (0,5,9)]
chord_sequence((c19,c19,c19),(m7,a6,sc),(3.,3.,3.),'example12')
