# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import numpy as np
#
#dimer1=open("C:\\Users\\amyjo\\Google Drive\\NC_locals\\Thesis_data\\Chap1-Building_the_model\\dimer\\Total_Energies_CH3_CH3.txt",'r')
#for line in dimer1:
#    rm=line.split('  ')
#    
#    

#!/usr/bin/env python
#import sys, os
#import numpy as np
import pandas as pd
import re

dimer1="C:\\Users\\amyjo\\Google Drive\\NC_locals\\Thesis_data\\Chap1-Building_the_model\\dimer\\Total_Energies_CH3_CH3.txt"

# Chekc file works / loads
#if [dimer1 == True]:
#    print ("yes")

f=open(dimer1,'r').readlines()
pi=(str(f))
#print(pi)
#print (type(f))

if match:
    print ("yes")
    items = match.groups()
    print (items)
else:
    print ("no")
#buffer=''
#if f:
#    for line in f:
#        buffer += line
#
##print (buffer, type(buffer))
#
##print (buffer.split('  '))
#        
#raw=re.split(r'\s{2,}', buffer)
##raw=buffer.split('  ')
#print (raw,type(raw))
##nn=(str(raw)).split('\\n')
#
##print (nn)
#
#df = pd.DataFrame(data=raw, columns=['col'])
##result = df.col.str.extract('([a-zA-Z]+)([^a-zA-Z]+)', expand=True)
##result.columns = ['Text', 'Number']
##print(result)
#
#
