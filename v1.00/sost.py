# -*- coding: utf-8 -*-
"""
N. Ahmad, S. Derrible, T. Eason, and H. Cabezas, 2016, “Using Fisher information to track stability in multivariate systems”,
Royal Society Open Science, 3:160582, DOI: 10.1098/rsos.160582
"""

import csv
import pandas as pd
import numpy as np

def SOST(f_name,s_for_sd):
    out=open(f_name+'.csv','rb')
    data=csv.reader(out)
    Data=[]
        
    for row in data:
        Data.append(row)
            
    out.close()
    
    Data_num=[]
    
    for row in Data:
        temp=[]
        for i in range(1,len(row)):
            if row[i]=='':
                temp.append(0)
            else:
                temp.append(float(row[i]))
        Data_num.append(temp)
        
    df=pd.DataFrame(Data_num)
    
    sos=[]
    for j in range(len(df.columns)):
        sos_temp=[]
        for i in df.index:
            A=list(df[j][i:i+s_for_sd])
            A_1=[float(i) for i in A if i!=0 ]
        
            
            if len(A_1)==s_for_sd:
                sos_temp.append(np.std(A_1,ddof=1))
                
       
        if len(sos_temp)==0:
            sos.append(0)
        else:
            
            sos.append(min(sos_temp)*2)
        
        
    df_sos=pd.DataFrame(sos)
    df_sos=df_sos.transpose()
    df_sos.to_csv('{}_sost.csv'.format(f_name),index=False,header=False)
   


        
    
    
