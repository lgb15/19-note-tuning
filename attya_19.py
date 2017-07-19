# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 12:56:16 2017

@author: budd
"""

import freqs_and_rats
import chord_sequence_new

roots_19 = [f19,2*bf19,2*bf19,ef19,ef19,ef19,ef19,af19,af19,af19,
         df19,df19,df19,df19,g19,g19,g19,c19,
         c19,f19,f19,bf19,bf19,bf19,bf19,ef19,ef19,ef19,
         0.5*af19,0.5*af19,0.5*af19,0.5*af19,d19,d19,2*a19,d19,d19,0.5*g19,0.5*d19,d19,g19,2*d19]
         
roots_12 = [f12,2*bf12,2*bf12,ef12,ef12,ef12,ef12,af12,af12,af12,
         df12,df12,df12,df12,g12,g12,g12,c12,
         c12,f12,f12,bf12,bf12,bf12,bf12,ef12,ef12,ef12,
         0.5*af12,0.5*af12,0.5*af12,0.5*af12,d12,d12,2*a12,d12,d12,0.5*g12,0.5*d12,d12,g12,2*d12]

ratios_19 = (min7_19c,min7_19c,min7_19a,dom7_19c,dom7_19c,dom7_19c,dom7_19c,maj7_19a,maj7_19c,maj7_19a,
          maj7_19c,maj7_19c,maj7_19c,maj7_19c,dom7_19a,dom7_19c,dom7_19a,maj7_19c,
          min7_19c,min7_19c,min7_19a,dom7_19c,dom7_19c,dom7_19c,dom7_19c,maj7_19a,maj7_19c,maj7_19a,
          maj7_19c,maj7_19c,maj7_19c,maj7_19c,dom7_19a,dom7_19b,dim_19,dom7_19b,dom7_19a,maj7_19c,[0],[1],[1],[1]
          )
          
ratios_12 = (min7_12c,min7_12c,min7_12a,dom7_12c,dom7_12c,dom7_12c,dom7_12c,maj7_12a,maj7_12c,maj7_12a,
          maj7_12c,maj7_12c,maj7_12c,maj7_12c,dom7_12a,dom7_12c,dom7_12a,maj7_12c,
          min7_12c,min7_12c,min7_12a,dom7_12c,dom7_12c,dom7_12c,dom7_12c,maj7_12a,maj7_12c,maj7_12a,
          maj7_12c,maj7_12c,maj7_12c,maj7_12c,dom7_12a,dom7_12b,dim_12,dom7_12b,dom7_12a,maj7_12c,[0],[1],[1],[1]
          )            
          
durations = (2.0,1.5,0.5,0.5,0.5,0.5,0.5,0.5,1.0,0.5,
             0.5,0.5,0.5,0.5,0.5,1.0,0.5,4.0,
             2.0,1.5,0.5,0.5,0.5,0.5,0.5,0.5,1.0,0.5,
             0.5,0.5,0.5,0.5,1/3,1/3,1/3,0.5,0.5,2.0,0.5,0.5,0.5,0.5
             )
             
filename_19 = 'attya_19chords'

filename_12 = 'attya_12chords'



lower_roots_12 = [i*0.25 for i in roots_12]

lower_roots_19 = [i*0.25 for i in roots_19]

