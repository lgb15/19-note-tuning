# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 12:04:53 2017

@author: budd
"""
# # # # #
#List of note frequencies for 12 and 19-tone ET regimes
# # # # #

# 12-note equal temperament #
a12 = 440.0
as12 = bf12 = 466.1637615180899
b12 = cf12 = 493.8833012561241
bs12 = c12 = 523.2511306011972
cs12 = df12 = 554.3652619537442
d12 = 587.3295358348151
ds12 = ef12 = 622.2539674441618
e12 = ff12 = 659.2551138257398
es12 = f12 = 698.4564628660078
fs12 = gf12 = 739.9888454232688
g12 = 783.9908719634985
gs12 = af12 = 830.6093951598903

# ratios between successive notes in 12tet #
ttet_ratios=[
1.0,
1.0594630943592953,
1.122462048309373,
1.189207115002721,
1.2599210498948732,
1.3348398541700344,
1.4142135623730951,
1.4983070768766815,
1.5874010519681994,
1.681792830507429,
1.7817974362806785,
1.8877486253633868
]

# difference in ratios between 12tet and just-intonation equivalent #
ttet_diff = [
0.0, 
0.007203572307371342, 
0.011350937198261857, 
0.010792884997278929, 
0.00992104989487319, 
0.0015065208367011085, 
0.007963562373095145, 
0.0016929231233184794, 
0.012598948031800727, 
0.015126163840762263, 
0.018202563719321496, 
0.012748625363386834
]

ttet_just_equiv = [
1,
16/15,
10/9,
6/5,
5/4,
4/3,
45/32,
3/2,
8/5,
5/3,
9/5,
15/8
]

# some common chord ratios for 12tet - a,b,c,d denotes inversions of the chords #
# major triads #
maj_12a = [ttet_ratios[0],ttet_ratios[4],ttet_ratios[7]]
maj_12b = [ttet_ratios[4],ttet_ratios[7],2*ttet_ratios[0]]
maj_12c = [ttet_ratios[7],2*ttet_ratios[0],2*ttet_ratios[4]]

# minor triads #
min_12a = [ttet_ratios[0],ttet_ratios[3],ttet_ratios[7]]
min_12b = [ttet_ratios[3],ttet_ratios[7],2*ttet_ratios[0]]
min_12c = [ttet_ratios[7],2*ttet_ratios[0],2*ttet_ratios[3]]

# dominant sevenths #
dom7_12a = [ttet_ratios[0],ttet_ratios[4],ttet_ratios[7],ttet_ratios[10]]
dom7_12b = [ttet_ratios[4],ttet_ratios[7],ttet_ratios[10],2*ttet_ratios[0]]
dom7_12c = [ttet_ratios[7],ttet_ratios[10],2*ttet_ratios[0],2*ttet_ratios[4]]
dom7_12d = [ttet_ratios[10],2*ttet_ratios[0],2*ttet_ratios[4],2*ttet_ratios[7]]

# minor sevenths #
min7_12a = [ttet_ratios[0],ttet_ratios[3],ttet_ratios[7],ttet_ratios[10]]
min7_12b = [ttet_ratios[3],ttet_ratios[7],ttet_ratios[10],2*ttet_ratios[0]]
min7_12c = [ttet_ratios[7],ttet_ratios[10],2*ttet_ratios[0],2*ttet_ratios[3]]
min7_12d = [ttet_ratios[10],2*ttet_ratios[0],2*ttet_ratios[3],2*ttet_ratios[7]]

# major sevenths #
maj7_12a = [ttet_ratios[0],ttet_ratios[4],ttet_ratios[7],ttet_ratios[11]]
maj7_12b = [ttet_ratios[4],ttet_ratios[7],ttet_ratios[11],2*ttet_ratios[0]]
maj7_12c = [ttet_ratios[7],ttet_ratios[11],2*ttet_ratios[0],2*ttet_ratios[4]]
maj7_12d = [ttet_ratios[11],2*ttet_ratios[0],2*ttet_ratios[4],2*ttet_ratios[7]]

# diminished and diminished sevenths #
dim_12 = [ttet_ratios[0],ttet_ratios[3],ttet_ratios[6]]
dim7_12 = [ttet_ratios[0],ttet_ratios[3],ttet_ratios[6],ttet_ratios[10]]

############################################################################

# 19-note equal temperament #
a19 = 440.0
as19 = 456.3482195563244
bf19 = 473.30385793688026
b19 = 490.8894838150792
bs19 = 509.1285044043967
c19 = 528.0451966143654
cs19 = 547.6647393641703
df19 = 568.0132470968582
d19 = 589.1178045387678
ds19 = 611.0065027504487
ef19 = 633.7084765170539
e19 = 657.2539431279737
es19 = 681.6742425973284
f19 = 707.0018793788565
fs19 = 733.2705656307191
gf19 = 760.515266087813
g19 = 788.7722446013131
gs19 = 818.0791124073976
af19 = 848.4748781893957

# ratios between successive notes in 19tet # 
ntet_ratios = [
1.0,
1.0371550444461919,
1.0756905862201824,
1.1156579177615435,
1.1571102372827198,
1.200102719578103,
1.2446925894640233,
1.290939197947405,
1.3389041012244722,
1.3886511426146562,
1.440246537538759,
1.4937589616544857,
1.5492596422666556,
1.606822453133765,
1.666524012797089,
1.7284437865632112,
1.7926641922757116,
1.8592707100168127,
1.9283519958849902
]

# difference in ratios between 19tet and just-intonation equivalent #
ntet_diff = [
0.0, 
0.0045116222204748535, 
0.00902391955351578, 
0.004546806650432389, 
0.014764762717280222, 
0.0001027195781031498, 
0.00530741053597672, 
0.010939197947404944, 
0.005570767891138972, 
0.017598857385343836, 
0.0180243153165367, 
0.00624103834551426, 
0.10925964226665563, 
0.006822453133764839, 
0.00014265386957768023, 
0.021777119896544406, 
0.0073358077242884345, 
0.015729289983187345, 
0.008351995884990249
]

ntet_just_equiv = [
1,
25/24,
16/15,
10/9,
75/64,
6/5,
5/4,
32/25,
4/3,
45/32,
64/45,
3/2,
36/25,
8/5,
5/3,
128/75,
9/5,
15/8,
48/25
]
 
# some common chord ratios for 19tet#
maj_19a = [ntet_ratios[0],ntet_ratios[6],ntet_ratios[11]]
maj_19b = [ntet_ratios[6],ntet_ratios[11],2*ntet_ratios[0]]
maj_19c = [ntet_ratios[11],2*ntet_ratios[0],2*ntet_ratios[6]]

min_19a = [ntet_ratios[0],ntet_ratios[5],ntet_ratios[11]]
min_19b = [ntet_ratios[5],ntet_ratios[11],2*ntet_ratios[0]]
min_19c = [ntet_ratios[11],2*ntet_ratios[0],2*ntet_ratios[5]]

dom7_19a = [ntet_ratios[0],ntet_ratios[6],ntet_ratios[11],ntet_ratios[16]]
dom7_19b = [ntet_ratios[6],ntet_ratios[11],ntet_ratios[16],2*ntet_ratios[0]]
dom7_19c = [ntet_ratios[11],ntet_ratios[16],2*ntet_ratios[0],2*ntet_ratios[6]]
dom7_19d = [ntet_ratios[16],2*ntet_ratios[0],2*ntet_ratios[6],2*ntet_ratios[11]]

min7_19a = [ntet_ratios[0],ntet_ratios[5],ntet_ratios[11],ntet_ratios[16]]
min7_19b = [ntet_ratios[5],ntet_ratios[11],ntet_ratios[16],2*ntet_ratios[0]]
min7_19c = [ntet_ratios[11],ntet_ratios[16],2*ntet_ratios[0],2*ntet_ratios[5]]
min7_19d = [ntet_ratios[16],2*ntet_ratios[0],2*ntet_ratios[5],2*ntet_ratios[11]]

maj7_19a = [ntet_ratios[0],ntet_ratios[6],ntet_ratios[11],ntet_ratios[17]]
maj7_19b = [ntet_ratios[6],ntet_ratios[11],ntet_ratios[17],2*ntet_ratios[0]]
maj7_19c = [ntet_ratios[11],ntet_ratios[17],2*ntet_ratios[0],2*ntet_ratios[6]]
maj7_19d = [ntet_ratios[17],2*ntet_ratios[0],2*ntet_ratios[6],2*ntet_ratios[11]]

dim_19 = [ntet_ratios[0], ntet_ratios[5], ntet_ratios[10]]
dim7_19 = [ntet_ratios[0], ntet_ratios[5], ntet_ratios[10],ntet_ratios[16]]