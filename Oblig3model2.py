#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
#
C = 1e-10
R = 1e11
r = 1e6
V0 = 100e-3
E = 50e-3 #Batteriets spenning
# Spenningspuls
def Vs(t,V0,t0):
    return V0*np.sin(2*np.pi*t/t0)
# Simuleringsparameter
RC = R*C
rC = r*C
dt = 0.1*rC
T = RC/100.0
t0 = T*0.1
nsteps = int(T/dt)
L = 100
V = np.zeros((nsteps,L))
t = np.zeros((nsteps,1))
V[0,0] = V0
#løser kabellikningen for hvert tidssteg og posisjon. 
for j in range(0,nsteps-1):
    t[j+1] = t[j] + dt
    V[j+1,0] = Vs(t[j+1],V0,t0)
    for i in range(1,L-1):
        V[j+1,i] = V[j,i] + dt*(-(V[j,i]+E)/RC + (V[j,i+1]-2*V[j,i]+V[j,i-1])/rC)
    V[j+1,L-1] = V[j,L-1] + dt*(-(V[j,L-1]+E)/RC + (-V[j,L-1]+V[j,L-2])/rC)


# In[4]:


for i in range(0,L-1,20):
    plt.figure(figsize=(10,5))
    plt.plot(t, V[:, i])
    plt.ylabel('Amplitude of signal')
    plt.xlabel('Time')
plt.figure(figsize=(10,5))
plt.plot(t, V[:, L-1])
plt.ylabel('Amplitude of signal')
plt.xlabel('Time')


# In[ ]:




