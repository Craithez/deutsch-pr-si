"""
BARNSLEY FERN

By: it's literally monique
"""

import matplotlib.pyplot as plt 
from random import randint 
  
x = [0] 
y = [0] 

for i in range(0, 50000): 
  
    z = randint(1, 100) 
      
    if z == 1: 
        x.append(0) 
        y.append(0.16*(y[i])) 
         
    if z>= 2 and z<= 86: 
        x.append(0.85*(x[i]) + 0.04*(y[i])) 
        y.append(-0.04*(x[i]) + 0.85*(y[i])+1.6) 
      
    if z>= 87 and z<= 93: 
        x.append(0.2*(x[i]) - 0.26*(y[i])) 
        y.append(0.23*(x[i]) + 0.22*(y[i])+1.6) 
          
    if z>= 94 and z<= 100: 
        x.append(-0.15*(x[i]) + 0.28*(y[i])) 
        y.append(0.26*(x[i]) + 0.24*(y[i])+0.44) 


plt.scatter(x, y, s = 0.2, c ='#5dbb63') 
plt.axis("off")
plt.savefig('barnsley_fern.png', dpi=300, bbox_inches='tight')
plt.show()