# -*- coding: utf-8 -*-
"""
N. Ahmad, S. Derrible, T. Eason, and H. Cabezas, 2016, “Using Fisher information to track stability in multivariate systems”,
Royal Society Open Science, 3:160582, DOI: 10.1098/rsos.160582
"""

import datetime
import os

Time=datetime.datetime.now()

f_name=raw_input('enter file name-')
w_size=int(input('enter window size-'))
w_incre=int(input('enter window increment-'))
sm_step=int(input('enter step for block average for smoothing of the FI-'))
X_tick=raw_input('Provide step for xticks(Y)-')
if X_tick.upper()=='Y':
    xtick_step=int(input('enter step for xticks-'))
else:
    xtick_step='def'
def main(f_name,w_size,w_incre,xtick_step):
    
    if raw_input('''Want to use default size of state? enter Y 
    otherwise enter N and provide a .csv file named 'file name'_sost.csv-''')=='Y':
        from sost import SOST
        SOST(f_name,w_size)
    from fisher import FI
    FI(f_name,w_size,w_incre)
    
    from smooth import FI_smooth
    FI_smooth(f_name,sm_step,w_size,xtick_step)

main(f_name,w_size,w_incre,xtick_step)
os.remove('FI.csv')
print ('Total time taken-',datetime.datetime.now()-Time)
