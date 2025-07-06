import pandas as pd
import numpy as np
import math
import os
import matplotlib.pyplot as plt
#%matplotlib inline

import warnings
warnings.filterwarnings('ignore')
from tqdm import tqdm

import tkinter as tk
from tkinter import messagebox



def AuNP_virtual(no_layer,x_size,y_size,a):
    
    item = []
    number=0
    tol1 = a/2
    tol_vs_111 = a/6
    vs_111 = np.array([1,2,4,5])
    
    for l in range(no_layer):        
        for i in range(x_size):
            for j in range(y_size):
                if l%2 == 0:
                    if i%2 == 0:
                        
                        x_cord = i*(tol1)  # shift lattice with x direction with lattice constant a,for Au take 0.269nm
                        y_cord = j*a
                        z_cord = (l*(a/2))
                        atom_name = "AUB"

                        if i<(x_size-2):
                            
                            x_vs_100 = i*(tol1)+(tol1)    # Virtual Sites (100)
                            y_vs_100 = j*a
                            z_vs_100 = (l*(a/2))
                            atom_name_vs_100 = "AI0"
                            
                            if j<(y_size-1):
                                if l<(no_layer-1):

                                    vs_111_32 = []    # List containing 32 (111) virtual sites

                                    for m in vs_111:         # Adding (111) Virtual Sites
                                        for n in vs_111:
                                            for o in vs_111:
                                                if (m+n+o)%2 == 0 :
                                                    x_vs_111 = (m * tol_vs_111) + (x_cord)
                                                    y_vs_111 = (n * tol_vs_111) + (y_cord)
                                                    z_vs_111 = (o * tol_vs_111) + (z_cord)
                                                    atom_name_vs_111 = "AI1"
                                                    atom_vs_111 = [atom_name_vs_111, number, x_vs_111, y_vs_111, z_vs_111]
                                                    vs_111_32.append(atom_vs_111)
                                                    number += 1


                        
                    else:
                        if j < (y_size-1):
                            if i < (x_size-1):
                                
                                x_cord = i*(tol1)
                                y_cord = (j*a)+(tol1) # to create face centered lattice in XY plane, shift a/2 with step a
                                z_cord = (l*(a/2))
                                atom_name = "AUB"


                            x_vs_100 = i*(tol1)-(tol1)
                            y_vs_100 = (j*a)+(tol1)   # Virtual Sites (100)
                            z_vs_100 = (l*(a/2))
                            atom_name_vs_100 = "AI0" 

                else:
                    if i%2 == 0:
                        
                        if j < (y_size-1):
                            if i < (x_size-1):
                                
                                x_cord = i*(tol1)  #shift lattice with x direction with lattice constant a,for Au take 0.269nm
                                y_cord = (j*a)+tol1
                                z_cord = l*(a/2)
                                atom_name = "AUB"
##This block of code generate a central atom at the center of the cube
#                             if i < (x_size-2):
#                                 x_vs_100 = i*(tol1)+(tol1)  # Virtual Sites (100)
#                                 y_vs_100 = (j*a)+(tol1)
#                                 z_vs_100 = l*(a/2)
#                                 atom_name_vs_100 = "AI0"
                        
                        
                    else:
                            if i<(x_size-2):
                                x_cord = i*(tol1)
                                y_cord = (j*a) #to create face centered lattice in XY plane, shift a/2 with step a
                                z_cord = l*(a/2)
                                atom_name = "AUB"

                            x_vs_100 = i*(tol1)-(tol1)
                            y_vs_100 = (j*a) # Virtual Sites (100)
                            z_vs_100 = l*(a/2)
                            atom_name_vs_100 = "AI0"

                atom = [atom_name,number,x_cord,y_cord,z_cord]
                atom_vs_100 = [atom_name_vs_100,number,x_vs_100,y_vs_100,z_vs_100]
                item.extend(vs_111_32)
                item.append(atom)
                item.append(atom_vs_100)                
                number += 2
    return item

### For non polarised one
def AuNP(no_layer,x_size,y_size,a):
    
    item = []
    number=0
    tol1 = a/2
    
    for l in range(no_layer):        
        for i in range(x_size):
            for j in range(y_size):
                if l%2 == 0:
                    if i%2 == 0:
                        
                        x_cord = i*(tol1)  # shift lattice with x direction with lattice constant a,for Au take 0.269nm
                        y_cord = j*a
                        z_cord = (l*(a/2))
                        atom_name = "AUB"
                                                
                    else:
                        if j < (y_size-1):
                            if i < (x_size-1):
                                
                                x_cord = i*(tol1)
                                y_cord = (j*a)+(tol1) # to create face centered lattice in XY plane, shift a/2 with step a
                                z_cord = (l*(a/2))
                                atom_name = "AUB"

                else:
                    if i%2 == 0:
                        
                        if j < (y_size-1):
                            if i < (x_size-1):
                                
                                x_cord = i*(tol1)  #shift lattice with x direction with lattice constant a,for Au take 0.269nm
                                y_cord = (j*a)+tol1
                                z_cord = l*(a/2)
                                atom_name = "AUB"
##This block of code generate a central atom at the center of the cube
#                             if i < (x_size-2):
#                                 x_vs_100 = i*(tol1)+(tol1)  # Virtual Sites (100)
#                                 y_vs_100 = (j*a)+(tol1)
#                                 z_vs_100 = l*(a/2)
#                                 atom_name_vs_100 = "AI0"
                        
                        
                    else:
                            if i<(x_size-2):
                                x_cord = i*(tol1)
                                y_cord = (j*a) #to create face centered lattice in XY plane, shift a/2 with step a
                                z_cord = l*(a/2)
                                atom_name = "AUB"                            

                atom = [atom_name,number,x_cord,y_cord,z_cord]
                item.append(atom)                
                number += 2
    return item



def spacer(var, space, pref):
    
    temp = str(var)
    if(len(temp)) >= space:
        out = temp[len(temp)-space:]
    else:
        if(pref == 'r'):
            out = ('{:>5}'.format(temp))
        else:
            out = ('{:<5}'.format(temp))
    return out

def dump_pos(df, delta):
    ind=[]
    for i in range(len(df_111)):
        if df_111['plane'].iloc[i] >= df_111['Z'].iloc[i]:
            ind.append(i)
        elif np.abs(df_111['Z'].iloc[i]-df_111['plane'].iloc[i]) < delta:
            ind.append(i)
    return ind
def dump_neg(df, delta):
    ind=[]
    for i in range(len(df_111)):
        if df_111['plane'].iloc[i] <= df_111['Z'].iloc[i]:
            ind.append(i)
        elif np.abs(df_111['Z'].iloc[i]-df_111['plane'].iloc[i]) < delta:
            ind.append(i)
    return ind



from tkinter import simpledialog

# Function to get input values
def get_inputs():
    gamma = simpledialog.askfloat("Input", "Enter the value of surface area ratio \n Choose 1 to 3.5:")
    d = simpledialog.askfloat("Input", "Enter diameter of the nanoparticle:\t")
    return gamma, d

# Create main window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Get inputs from user
gamma, d = get_inputs()

# Now you can use gamma and d in your calculations
print("Surface area ratio :", gamma)
print("Diameter of the nanoparticle:", d)
#import streamlit as st

#st.title("Nanoparticle Surface Area Calculator")

#gamma = st.number_input("Enter the value of surface area ratio (2 or 2.5):", min_value=0.0, max_value=10.0, value=2.0)
#d = st.number_input("Enter diameter of the nanoparticle:", min_value=0.0, value=10.0)

#if st.button("Calculate"):
#    st.write(f"Surface area ratio: {gamma}")
#    st.write(f"Diameter of the nanoparticle: {d}")

#import dash
#from dash import dcc, html
#from dash.dependencies import Input, Output

# Your existing complex computation function
#def complex_computation(gamma, d):
    # Replace this with your actual computation logic
#    result = gamma * d  # Example of a calculation
#    return result
#gamma = int(input("enter the value of surface area ratio: ")) ##ratio of the surface area between (111):(100)
#d = float(input("enter diameter of the nanoparticle: ")) ##diameter of the nanopartile to model
a = 0.40782 ## lattice parameter for gold nanoparticle
t1 = np.sqrt(3.0*gamma+(3.0*np.sqrt(3)))
t2 = 3.0*gamma+(2.0*np.sqrt(3))
nx = np.round((np.round(d/a)*t1*(t1+np.sqrt(np.sqrt(3.0))))/t2)
nx

a = 0.40782
x = y = z = int(nx)
# x = 10
# y = 10
# z = 10

no_layer = (z*2)+1
x_size = (x*2)+2
y_size = y+1



atoms = AuNP_virtual(no_layer, x_size, y_size, a)
#atoms = AuNP(no_layer, x_size, y_size, a)

##Converting to numpy arrays
arr = np.array(atoms)
## removing duplicate arrays, created because of looping
unique_indices = np.unique(arr[:, 2:], axis=0, return_index=True)[1]
arr1 = arr[unique_indices]
len(arr1)

arr1[:,2:] = arr1[:,2:].astype(float)
arr1[:,1] = arr1[:,1].astype(int)
arr1[:,1].astype(int)


#removing duplicate atoms
df = pd.DataFrame(atoms, columns=['atom', 'number', 'X', 'Y', 'Z'])
len(df)
box_x = box_y = box_z = df['X'].max()

df = df.drop_duplicates(subset=['X','Y','Z'])
df.reset_index(drop=True, inplace=True)
len(df)

df['atom'].value_counts()

df.describe()

D = df['Z'].max() / 2
df['X'] = df['X']-D
df['Y'] = df['Y']-D
df['Z'] = df['Z']-D
df['X'].median(), df['Y'].median(), df['Z'].median()

df_111 = df.copy()
delta = 0.0001

print("started cutting plane-1 of (111)")
df_111['plane'] = D + df_111['X'] + df_111['Y']
temp1=[]
temp11=[]
for i in tqdm(range(len(df_111)),colour='green'):
    if (df_111['plane'].iloc[i] > df_111['Z'].iloc[i]\
        or np.abs(df_111['Z'].iloc[i]-df_111['plane'].iloc[i]) < delta):
        temp1.append(i)
  
for i in range(len(df_111)):
    if (df_111['plane'].iloc[i] == df_111['Z'].iloc[i]\
        or np.abs(df_111['Z'].iloc[i]-df_111['plane'].iloc[i]) < delta):
        temp11.append(i)
        
df_111 = df_111.iloc[temp1]
len(df_111)

for i in temp1:
    if i in temp11 and i in df_111.index:
        atom_value = df_111.at[i, 'atom']
        if atom_value == "AUB":
            df_111.at[i, 'atom'] = "AUS"
        elif atom_value == "AI0":
            df_111.at[i, 'atom'] = "AS0"
        elif atom_value == "AI1":
            df_111.at[i, 'atom'] = "AS1"    
df_111.reset_index(drop=True, inplace=True)

print("started cutting plane-2 of (111)")
df_111['plane'] = D + df_111['X'] - df_111['Y']
temp2=[]
temp22=[]
for i in tqdm(range(len(df_111)),colour='green'):
    if (df_111['plane'].iloc[i] > df_111['Z'].iloc[i]\
        or np.abs(df_111['Z'].iloc[i]-df_111['plane'].iloc[i]) < delta):
        temp2.append(i)
  
for i in range(len(df_111)):
    if (df_111['plane'].iloc[i] == df_111['Z'].iloc[i]\
        or np.abs(df_111['Z'].iloc[i]-df_111['plane'].iloc[i]) < delta):
        temp22.append(i)
        
df_111 = df_111.iloc[temp2]

for i in temp2:
    if i in temp22 and i in df_111.index:
        atom_value = df_111.at[i, 'atom']
        if atom_value == "AUB":
            df_111.at[i, 'atom'] = "AUS"
        elif atom_value == "AI0": 
            df_111.at[i, 'atom'] = "AS0"
        elif atom_value == "AI1":
            df_111.at[i, 'atom'] = "AS1"
df_111.reset_index(drop=True, inplace=True)

print("started cutting plane-3 of (111)")
df_111['plane'] = D - df_111['X'] - df_111['Y']
temp3=[]
temp33=[]
for i in tqdm(range(len(df_111))):
    if (df_111['plane'].iloc[i] > df_111['Z'].iloc[i]\
        or np.abs(df_111['Z'].iloc[i]-df_111['plane'].iloc[i]) < delta):
        temp3.append(i)
  
for i in range(len(df_111)):
    if (df_111['plane'].iloc[i] == df_111['Z'].iloc[i]\
        or np.abs(df_111['Z'].iloc[i]-df_111['plane'].iloc[i]) < delta):
        temp33.append(i)
        
df_111 = df_111.iloc[temp3]
len(df_111)
for i in temp3:
    if i in temp33 and i in df_111.index:
        atom_value = df_111.at[i, 'atom']
        if atom_value == "AUB":
            df_111.at[i, 'atom'] = "AUS"
        elif atom_value == "AI0":
            df_111.at[i, 'atom'] = "AS0"
        elif atom_value == "AI1":
            df_111.at[i, 'atom'] = "AS1"
df_111.reset_index(drop=True, inplace=True)

print("started cutting plane-4 of (111)")
df_111['plane'] = D - df_111['X'] + df_111['Y']
# df_111 = df_111.iloc[dump_pos(df_111,0.0001)]  
# len(df_111)
temp4=[]
temp44=[]
for i in tqdm(range(len(df_111)),colour='green'):
    if (df_111['plane'].iloc[i] > df_111['Z'].iloc[i]\
        or np.abs(df_111['Z'].iloc[i]-df_111['plane'].iloc[i]) < delta):
        temp4.append(i)
  
for i in range(len(df_111)):
    if (df_111['plane'].iloc[i] == df_111['Z'].iloc[i]\
        or np.abs(df_111['Z'].iloc[i]-df_111['plane'].iloc[i]) < delta):
        temp44.append(i)
        
df_111 = df_111.iloc[temp4]
len(df_111)
for i in temp4:
    if i in temp44 and i in df_111.index:
        atom_value = df_111.at[i, 'atom']
        if atom_value == "AUB":
            df_111.at[i, 'atom'] = "AUS"
        elif atom_value == "AI0":
            df_111.at[i, 'atom'] = "AS0"
        elif atom_value == "AI1":
            df_111.at[i, 'atom'] = "AS1"

df_111.reset_index(drop=True, inplace=True)

print("started cutting plane-5 of (111)")
df_111['plane'] = - D - df_111['X'] - df_111['Y']
# df_111 = df_111.iloc[dump_neg(df_111,0.0001)] 
# len(df_111)
temp5=[]
temp55=[]
for i in tqdm(range(len(df_111)),colour='green'):
    if (df_111['plane'].iloc[i] < df_111['Z'].iloc[i]\
        or np.abs(df_111['Z'].iloc[i]-df_111['plane'].iloc[i]) < delta):
        temp5.append(i)
  
for i in range(len(df_111)):
    if (df_111['plane'].iloc[i] == df_111['Z'].iloc[i]\
        or np.abs(df_111['Z'].iloc[i]-df_111['plane'].iloc[i]) < delta):
        temp55.append(i)
        
df_111 = df_111.iloc[temp5]
len(df_111)
for i in temp5:
    if i in temp55 and i in df_111.index:
        atom_value = df_111.at[i, 'atom']
        if atom_value == "AUB":
            df_111.at[i, 'atom'] = "AUS"
        elif atom_value == "AI0":
            df_111.at[i, 'atom'] = "AS0"
        elif atom_value == "AI1":
            df_111.at[i, 'atom'] = "AS1"

df_111.reset_index(drop=True, inplace=True)

print("started cutting plane-6 of (111)")

df_111['plane'] = - D - df_111['X'] + df_111['Y']
# df_111 = df_111.iloc[dump_neg(df_111,0.0001)] 
# len(df_111)
temp6=[]
temp66=[]
for i in tqdm(range(len(df_111)),colour='green'):
    if (df_111['plane'].iloc[i] < df_111['Z'].iloc[i]\
        or np.abs(df_111['Z'].iloc[i]-df_111['plane'].iloc[i]) < delta):
        temp6.append(i)
  
for i in range(len(df_111)):
    if (df_111['plane'].iloc[i] == df_111['Z'].iloc[i]\
        or np.abs(df_111['Z'].iloc[i]-df_111['plane'].iloc[i]) < delta):
        temp66.append(i)
        
df_111 = df_111.iloc[temp6]
len(df_111)
for i in temp6:
    if i in temp66 and i in df_111.index:
        atom_value = df_111.at[i, 'atom']
        if atom_value == "AUB":
            df_111.at[i, 'atom'] = "AUS"
        elif atom_value == "AI0":
            df_111.at[i, 'atom'] = "AS0"
        elif atom_value == "AI1":
            df_111.at[i, 'atom'] = "AS1"
df_111.reset_index(drop=True, inplace=True)

print("started cutting plane-7 of (111)")
df_111['plane'] = - D + df_111['X'] + df_111['Y']
# df_111 = df_111.iloc[dump_neg(df_111,0.0001)]  
# len(df_111)
temp7=[]
temp77=[]
for i in tqdm(range(len(df_111)),colour='green'):
    if (df_111['plane'].iloc[i] < df_111['Z'].iloc[i]\
        or np.abs(df_111['Z'].iloc[i]-df_111['plane'].iloc[i]) < delta):
        temp7.append(i)
  
for i in range(len(df_111)):
    if (df_111['plane'].iloc[i] == df_111['Z'].iloc[i]\
        or np.abs(df_111['Z'].iloc[i]-df_111['plane'].iloc[i]) < delta):
        temp77.append(i)
        
df_111 = df_111.iloc[temp7]
len(df_111)
for i in temp7:
    if i in temp77 and i in df_111.index:
        atom_value = df_111.at[i, 'atom']
        if atom_value == "AUB":
            df_111.at[i, 'atom'] = "AUS"
        elif atom_value == "AI0": 
            df_111.at[i, 'atom'] = "AS0"
        elif atom_value == "AI1":
            df_111.at[i, 'atom'] = "AS1"
df_111.reset_index(drop=True, inplace=True)

print("started cutting plane-8 of (111)")
df_111['plane'] = - D + df_111['X'] - df_111['Y']
# df_111 = df_111.iloc[dump_neg(df_111,0.0001)]   
# len(df_111)
temp8=[]
temp88=[]
for i in tqdm(range(len(df_111)),colour='green'):
    if (df_111['plane'].iloc[i] < df_111['Z'].iloc[i]\
        or np.abs(df_111['Z'].iloc[i]-df_111['plane'].iloc[i]) < delta):
        temp8.append(i)
  
for i in range(len(df_111)):
    if (df_111['plane'].iloc[i] == df_111['Z'].iloc[i]\
        or np.abs(df_111['Z'].iloc[i]-df_111['plane'].iloc[i]) < delta):
        temp88.append(i)
        
df_111 = df_111.iloc[temp8]
len(df_111)
for i in temp8:
    if i in temp88 and i in df_111.index:
        atom_value = df_111.at[i, 'atom']
        if atom_value == "AUB":
            df_111.at[i, 'atom'] = "AUS"
        elif atom_value == "AI0": 
            df_111.at[i, 'atom'] = "AS0"
        elif atom_value == "AI1":
            df_111.at[i, 'atom'] = "AS1"

df_111.reset_index(drop=True, inplace=True)

H = (np.round(d/a)*a)/2.0 + 0.05
print(f"Cutting (100) plane at a distance {H} nm")

print("Started cutting plane-1 of (100)")
df_111['plane'] =  -H
temp9=[]
temp99=[]

for i in tqdm(range(len(df_111)),colour='red'):
    if (df_111['plane'].iloc[i] < df_111['Z'].iloc[i]\
        or np.abs(df_111['Z'].iloc[i]-df_111['plane'].iloc[i]) < delta):
        temp9.append(i)
for i in range(len(df_111)):
#     if (df_111['plane'].iloc[i] < df_111['Z'].iloc[i] and df_111['Z'].iloc[i] >df_111['plane1'].iloc[i] ):
            
    if (df_111['plane'].iloc[i] == df_111['Z'].iloc[i] or np.abs(df_111['Z'].iloc[i]-df_111['plane'].iloc[i]) < 0.1):
        temp99.append(i)
df_111 = df_111.iloc[temp9]
len(df_111)
for i in temp9:
    if i in temp99 and i in df_111.index:
        atom_value = df_111.at[i, 'atom']
        if atom_value == "AUB":
            df_111.at[i, 'atom'] = "AUS"
        elif atom_value == "AI0":
            df_111.at[i, 'atom'] = "AS0"
        elif atom_value == "AI1":
            df_111.at[i, 'atom'] = "AS1"
df_111.reset_index(drop=True, inplace=True)

print("Started cutting plane-2 of (100)")
df_111['plane'] =  H
temp40=[]
temp404=[]
for i in tqdm(range(len(df_111)),colour='red'):
    if (df_111['plane'].iloc[i] > df_111['Z'].iloc[i]\
        or np.abs(df_111['Z'].iloc[i]-df_111['plane'].iloc[i]) < delta):
        temp40.append(i)
  
for i in range(len(df_111)):
    if (np.abs(df_111['Z'].iloc[i]-df_111['plane'].iloc[i]) < 0.1):
        temp404.append(i)
df_111 = df_111.iloc[temp40]
for i in temp40:
    if i in temp404 and i in df_111.index:
        atom_value = df_111.at[i, 'atom']
        if atom_value == "AUB":
            df_111.at[i, 'atom'] = "AUS"
        elif atom_value == "AI0":
            df_111.at[i, 'atom'] = "AS0"
        elif atom_value == "AI1":
            df_111.at[i, 'atom'] = "AS1"
df_111.reset_index(drop=True, inplace=True)

print("Started cutting plane-3 of (100)")
df_111['plane'] =  -H
temp10=[]
temp101=[]
for i in tqdm(range(len(df_111)),colour='red'):
    if (df_111['plane'].iloc[i] < df_111['Y'].iloc[i]\
        or np.abs(df_111['Y'].iloc[i]-df_111['plane'].iloc[i]) < delta):
        temp10.append(i)
  
for i in range(len(df_111)):
    if (np.abs(df_111['Y'].iloc[i]-df_111['plane'].iloc[i]) < 0.1):
        temp101.append(i)
df_111 = df_111.iloc[temp10]
for i in temp10:
    if i in temp101 and i in df_111.index:
        atom_value = df_111.at[i, 'atom']
        if atom_value == "AUB":
            df_111.at[i, 'atom'] = "AUS"
        elif atom_value == "AI0":
            df_111.at[i, 'atom'] = "AS0"
        elif atom_value == "AI1":
            df_111.at[i, 'atom'] = "AS1"
df_111.reset_index(drop=True, inplace=True)

print("Started cutting plane-4 of (100)")
df_111['plane'] =  H
temp20=[]
temp202=[]
for i in tqdm(range(len(df_111)),colour='red'):
    if (df_111['plane'].iloc[i] > df_111['Y'].iloc[i]\
        or np.abs(df_111['Y'].iloc[i]-df_111['plane'].iloc[i]) < delta):
        temp20.append(i)
  
for i in range(len(df_111)):
    if (np.abs(df_111['Y'].iloc[i]-df_111['plane'].iloc[i]) < 0.1):
        temp202.append(i)
df_111 = df_111.iloc[temp20]
len(df_111)
for i in temp20:
    if i in temp202 and i in df_111.index:
        atom_value = df_111.at[i, 'atom']
        if atom_value == "AUB":
            df_111.at[i, 'atom'] = "AUS"
        elif atom_value == "AI0" or atom_value == "AI1":
            df_111.at[i, 'atom'] = "AS0"
        elif atom_value == "AI1":
            df_111.at[i, 'atom'] = "AS1"
df_111.reset_index(drop=True, inplace=True)

print("Started cutting plane-5 of (100)")
df_111['plane'] = - H
temp30=[]
temp303=[]
for i in tqdm(range(len(df_111)),colour='red'):
    if (df_111['plane'].iloc[i] < df_111['X'].iloc[i]\
        or np.abs(df_111['X'].iloc[i]-df_111['plane'].iloc[i]) < delta):
        temp30.append(i)
  
for i in range(len(df_111)):
    if (np.abs(df_111['X'].iloc[i]-df_111['plane'].iloc[i]) < 0.1):
        temp303.append(i)
df_111 = df_111.iloc[temp30]
len(df_111)
for i in temp30:
    if i in temp303 and i in df_111.index:
        atom_value = df_111.at[i, 'atom']
        if atom_value == "AUB":
            df_111.at[i, 'atom'] = "AUS"
        elif atom_value == "AI0":
            df_111.at[i, 'atom'] = "AS0"
        elif atom_value == "AI1":
            df_111.at[i, 'atom'] = "AS1"
df_111.reset_index(drop=True, inplace=True)

print("Started cutting plane-6 of (100)")
df_111['plane'] =  H
temp50=[]
temp505=[]
for i in tqdm(range(len(df_111)),colour='red'):
    if (df_111['plane'].iloc[i] > df_111['X'].iloc[i]\
        or np.abs(df_111['X'].iloc[i]-df_111['plane'].iloc[i]) < delta):
        temp50.append(i)
  
for i in range(len(df_111)):
    if (np.abs(df_111['X'].iloc[i]-df_111['plane'].iloc[i]) < 0.1):
        temp505.append(i)
df_111 = df_111.iloc[temp50]
len(df_111)
for i in temp50:
    if i in temp505 and i in df_111.index:
        atom_value = df_111.at[i, 'atom']
        if atom_value == "AUB":
            df_111.at[i, 'atom'] = "AUS"
        elif atom_value == "AI0": 
            df_111.at[i, 'atom'] = "AS0"
        elif atom_value == "AI1":
            df_111.at[i, 'atom'] = "AS1"
df_111.reset_index(drop=True, inplace=True)

df2 = df_111[~df_111['atom'].isin(['AI1','AI0'])]
df2.reset_index(drop=True, inplace=True)
print(f"####Finished Cutting, now found {len(df2)} atoms")

print(df2['atom'].value_counts())

#corner_atoms = [404, 204, 269, 276, 387, 369, 224, 123, 47, 411, 60, 20, 36, 149, 274, 416, 408, 353, 215, 323, 194, 89, 115, 253]
#corner_atoms = [20, 79, 490, 1182, 120, 574, 1224, 64, 1786, 1070, 1162, 478,2128,2152,1882,1220,574,1806,1083,1024,1698,2135,2112,1012, 394]
##for 5.8nm 
#corner_atoms = [8419, 5111, 5119, 1835, 288, 144, 20, 1415, 4607, 7995, 4623, 4747, 8226, 9549, 9470, 9534, 8200, 4728, 1616, 4992, 5018, 9614, 167, 1634]
##for 7.4nm
#corner_atoms = [3352, 396, 196, 223, 20, 2732, 8893, 3031, 9079, 5661, 9485, 15661, 18310, 18210, 18430, 18329, 15982, 9669, 9679, 9515, 9102, 3053, 8911, 15358, 15691]

corner_atoms = []
len(corner_atoms)
df3 = df2.copy()

corner_indices = [idx for idx in corner_atoms if idx in df3.index]
df3.drop(corner_indices, inplace=True)

df3.reset_index(drop=True, inplace=True)
len(df3), len(df2)

filename = input("Enter output filename in .gro: \t")
with open(filename, "w") as gro_file:
    gro_file.write("Created in DN Lab\n{}\n".format(len(df3)))
    for i in range(len(df3)):
            residue_name = "LJS"
            name=df3['atom'][i]
            number=df3['number'][i]
            x=df3['X'][i]
            y=df3['Y'][i]
            z=df3['Z'][i]
            gro_file.write(f"{spacer(i+1,5,'r')}{spacer(residue_name,5,'l')}{spacer(name,5,'l')}{spacer(number,5,'r')}"
                           f"{x:8.3f}{y:8.3f}{z:8.3f}\n")
    gro_file.write(f"{box_x:10.5f}{box_x:10.5f}{box_x:10.5f}\n")


#command = f'vmd "{filename}"'

#os.system(command)
