# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 21:09:23 2019

@author: amyjo
"""
## This script takes the Total_Energies text file, and basically just formats it as a csv
## It then spits it back out, renamed, in the same folder as the source file. 
## MODIFICATIONS:
## File PATH
## To change from monomer, dimer to trimer, change the value of "mdt"

import pandas as pd
import re
import os,sys

#outdf=open("text.txt","w+")
mmer1="C:\\Users\\amyjo\\Google Drive\\NC_locals\\Thesis_data\\Chap1-Building_the_model\\dimer\\Total_Energies_OH_CH3.txt"

# Get the root filename, and get rid of the Total_Energies_ part, to fix naming convention for the output csv
csv_n=(os.path.basename(mmer1)).split('.')[0]

mdt="d"
csv_name=mdt+csv_n.replace("Total_Energies_","")
#print (csv_name)


f=open(mmer1,'r')
#data=(f.read())
data=(f.read()).split('\n')

#print (data,type(data))

#pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
df=pd.DataFrame(data)

# If you give them another two column names, it'll split into another 2 columns (i.e. 3 total)
#df[['Index','Energy']] = df[0].str.split("=",expand=True)

# Multiple column splits, first by "=" then ":"
#df=df[0].str.split('=|:',expand=True).add_prefix('Number_')

# Splitting into just 2 columns, from the first one - have to name your first column the same
df[[0,"Energy"]]=df[0].str.split('=',expand=True)

df["Energy"]=df["Energy"].str.strip()

df[["Energy","Units"]] = df["Energy"].str.split(" ",n=1,expand=True)

# This didn't work: Drop the empty rows (axis=0 is row, =1 is column)
#df.dropna(axis=0, how='all', thresh=None, subset=None, inplace=True)

##out.write(str(df))
#print(df.iloc[:15])
#print (df["Energy"])

#print (df)

#df.to_csv(csv_name)

out_path=re.sub(r"\\(?:.(?!\\))+$","",mmer1)+"\\"


#ask=input("Monomer, dimer or trimer? Type m / d /t .")
#
#if (ask == "m"):
#    out_csv='out_path+"\\m"+csv_name'
#elif (ask == "d"):
#    out_csv='out_path+"\\d"+csv_name'
#elif (ask == "t"):
#    out_csv='out_path+"\\t"+csv_name'
#else:
#    print("That wasn't an option, you numpty. Try again")
#    exit
#
#print (out_csv)
#
# This will output in the same place at the Jupyter notebook
#df.to_csv("dOH_CH3")

# This will output in the same place as source text file
final_file=((os.path.join(out_path,csv_name))+".csv")
df.to_csv(final_file)
#print(os.path.join(out_path,csv_name))

print (csv_name+" saved to "+final_file)

f.close()