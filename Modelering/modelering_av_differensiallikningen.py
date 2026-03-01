#%%

import numpy as np
import matplotlib.pyplot as plt


a = 0.3
e = 0.60
Q = 1367.7 / 4
sigma = 5.67 *10**(-8)

def f(T):
    return (1-a)*Q-e*sigma*T**4

T_verdier = np.linspace(250,350,1000)
jordens_temperatur = 16 + 273
plt.plot(T_verdier,f(T_verdier),color = "hotpink",label = "dT/dt")
plt.scatter(jordens_temperatur, f(jordens_temperatur),marker = "*", s = 200,color = "yellow",edgecolor = "black")
plt.grid(True)
plt.axhline(0, color='black', linewidth=1) # Vertikal linje (y-akse)
plt.title("Endring i jordens temperatur som funksjon av temperatur")
plt.xlabel("Temperatur (K)")
plt.ylabel("Temperaturendring per tidsenhet (dT/dt, K/s)")
plt.legend()

plt.show()