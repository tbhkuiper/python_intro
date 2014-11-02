from pylab import *

def T_change(sunlight, radiation_efficiency,temperature):
  return sunlight - radiation_efficiency*temperature
 
times = range(1000)
temperatures = []

temperature = 100.
radiation_efficiency = 0.01
for time in times:
  if time > 10:
    radiation_efficiency = 0.007
  temperature = temperature + T_change(1.,radiation_efficiency,temperature)
  temperatures.append(temperature)
  #print temperature

plot(times,temperatures)
show()