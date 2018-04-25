# -*- coding: utf-8 -*-
"""
N. Ahmad, S. Derrible, T. Eason, and H. Cabezas, 2016, “Using Fisher information to track stability in multivariate systems”,
Royal Society Open Science, 3:160582, DOI: 10.1098/rsos.160582
"""

import csv
import matplotlib.pyplot as plt
import pandas as pd

def FI_smooth(f_name,step,step_win,xtick_step):
    out=open('FI.csv','r')
    data=csv.reader(out)
    Data=[]
        
    for row in data:
        Data.append(row)
            
    out.close()
    
    FI=[]
    time=[]
    
    for row in Data:
        FI.append(eval(row[-2]))
        time.append(row[-1])
        
    FI_smth=[]
    
   
    for i in range(step,len(FI)+step,step):
        for j in range(i-step,i):
            FI_smth.append(float(sum(FI[i-step:i]))/len(FI[i-step:i]))
            
    FI_smth=FI_smth[0:len(FI)]
            

    plt.plot(range(step_win,len(FI_smth)+step_win),FI_smth,'r',label='Smoothed')
    plt.xlabel('Time Step')
    plt.ylabel('Fisher Information')
    
    if xtick_step!='def':
        plt.xticks(range(step_win,len(FI_smth)+step_win,xtick_step),
                [time[i] for i in range(0,len(FI_smth),xtick_step)],rotation=75)
                
    else:
        plt.xticks(range(step_win,len(FI_smth)+step_win,3),
                [time[i] for i in range(0,len(FI_smth),3)],rotation=75)
        
    plt.legend()
    plt.tight_layout()
    plt.savefig(f_name+'_FI'+'.pdf')
    plt.savefig(f_name+'_FI'+'.png',dpi=1000)
    plt.close('all')
    
    
    out=open('FI.csv','r')
    data=csv.reader(out)
    Data=[]
        
    for row in data:
        Data.append(row)
            
    out.close()
    
    for i in range(len(Data)):
        Data[i].append(FI_smth[i])
    
#    out=open("%s_FI.csv"%(f_name),"w")
#    new=csv.writer(out)
#    
#
#    new.writerow(['Time_Step','FI','Smooth_FI'])
    data_final=[]
    for i in Data:
        data_temp=[i[-2],i[-3],i[-1]]
        data_final.append(data_temp)
    
    df_final=pd.DataFrame(data_final)
    df_final.columns=['Time_Step','FI','Smooth_FI']
    df_final.to_csv("%s_FI.csv"%(f_name))
        
    #out.close()
