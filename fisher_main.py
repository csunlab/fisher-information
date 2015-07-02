# -*- coding: utf-8 -*-
"""
Citation: N. Ahmad, S. Derrible, T. Eason, and H. Cabezas, 2015, “Using Fisher Information In Big Data” 
(stored on arXiv, URL will be updated when finalized)
"""

import datetime

Time=datetime.datetime.now()

f_name=raw_input('enter file name-')
w_size=int(input('enter window size-'))
w_incre=int(input('enter window increment-'))
sm_step=int(input('enter step for block average for smoothing of the FI-'))
def main(f_name,w_size,w_incre):
    
    if raw_input('''Want to use default size of state? enter Y 
    otherwise enter N and provide a .csv file named sost.csv-''')=='Y':
        from sost import SOST
        SOST(f_name,w_size)
    from fisher import FI
    FI(f_name,w_size,w_incre)
    
    from smooth import FI_smooth
    FI_smooth(f_name,sm_step,w_size)


main(f_name,w_size,w_incre)
print 'Total time taken-',datetime.datetime.now()-Time