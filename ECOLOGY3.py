"""
http://nature.berkeley.edu/~bingxu/UU/geocomp/Week8/Predator-Prey%20Models.ppt
http://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equation
"""
from pylab import *

F = 100 # Initial fish population
S = 2   # Initial shark population
a = 100   # reproduction rate of the small fish
b = 2   # shark consumption rate
c =  .5 # small fish nutritional value
d =  10 # death rate of the sharks
dt= .01 # time step increment

times  = range(10)
fish   = []
sharks = []

for t in times:
  print F,S
  fish.append(F)
  sharks.append(S)
  dF = F*(a - b*S)*dt
  dS = S*(c*F - d)*dt
  print dF,dS
  new_F = max(F+dF,0)
  new_S = max(S+dS,0)
  F = int(round(new_F))
  S = int(round(new_S))

print times
print fish
print sharks
semilogy(times,fish,  label="Fish")
semilogy(times,sharks,label="Sharks")
legend()
show()
