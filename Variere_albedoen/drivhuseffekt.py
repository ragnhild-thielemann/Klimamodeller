#%%

import numpy as np
import matplotlib.pyplot as plt



T_verdier = np.linspace(220,310,1000) #tar temperaturer i kelvin fra 220 K - 310 K (tilsvarer intervallet fra -53 C til 37 C

#konstanter
sigma = 5.67*10**(-8) #Stefan–Boltzmann konstant
e = 0.66 #konstant som måler drivhuseffekten. En konstant 0<e<1
R = 6378*10**3 #jordens radius
S = 1376.6 #innkommene stråling fra sola

def a(T):
    return 0.7 - 0.5 * (np.exp((T - 265)/5) / (1 + np.exp((T - 265)/5)))

def incoming_energy(T):
    return np.pi * R**2 * S * (1 - a(T))

def outgoing_energy(T):
    return 4 * np.pi * R**2 * e * sigma * T**4


plt.plot(T_verdier,incoming_energy(T_verdier),label = "Innkommen varmeenergi fra sola",color = "hotpink")
plt.plot(T_verdier,outgoing_energy(T_verdier),label = "Utgående varmeenergi fra jorda")
plt.xlabel("Temperatur (K)")
plt.ylabel("Energi (W)")
plt.title("Drivhuseffekten på jordens klimabalanse") 
plt.grid(True)
plt.legend()


plt.show()