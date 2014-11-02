from pylab import *
 
 
times = range(100)
rabbit_population = []
wolf_population = []
rabbits = 10
wolves = 2

def rabbit_change(rabbits,wolves):
  change = rabbits - rabbits*wolves/10. -rabbits/100.
  return round(change)

def wolf_change(rabbits,wolves):
  change = rabbits*wolves/10. - wolves
  return round(change)

for time in times:
  wolves  = wolves + wolf_change(rabbits,wolves)
  if wolves < 0:
    wolves = 0
  rabbits = rabbits + rabbit_change(rabbits,wolves)
  if rabbits < 0:
    rabbits = 0
  print rabbits, wolves
  rabbit_population.append(rabbits)
  wolf_population.append(wolves)

plot(times,rabbit_population,label="Rabbits")
plot(times,wolf_population,label="Wolves")
show()
