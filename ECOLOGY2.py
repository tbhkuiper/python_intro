
from pylab import *

def change(prey_growth_rate,
           food_supply,
           number_of_prey,
           predation_rate,
           predator_death_rate,
           number_of_predators):
  prey_change = int(round(  prey_growth_rate*food_supply
                 - predation_rate*number_of_predators)) * number_of_prey
  predator_death_rate = max(min_predator_death_rate,
                            number_of_prey/(number_of_prey-number_of_predators))
  predator_change  = int(round(  predation_rate*number_of_prey
                      - predator_death_rate/number_of_prey)) * number_of_predators
  return prey_change, predator_change

food_supply             = float(raw_input("Food supply=                "))
prey_growth_rate        = float(raw_input("Prey growth rate=           "))
predation_rate          = float(raw_input("Predation rate=             "))
min_predator_death_rate = float(raw_input("Predator death rate=        "))
number_of_prey          =   int(raw_input("Initial prey population=    "))
number_of_predators     =   int(raw_input("Initial predator population="))

times = range(10)
predators = []
prey = []

for t in times:
  print "t=%2d    prey=%6d     predators=%6d" % (t,
                                                 number_of_prey,
                                                 number_of_predators)
  prey_change, predator_change = change(prey_growth_rate,
                                        food_supply,
                                        number_of_prey,
                                        predation_rate,
                                        min_predator_death_rate,
                                        number_of_predators)
  number_of_prey += prey_change
  if number_of_prey < 0:
    number_of_prey = 0
  number_of_predators += predator_change
  if number_of_predators < 0:
    number_of_predators = 0
  predators.append(number_of_predators)
  prey.append(number_of_prey)

plot(times,prey,label="Rabbits")
plot(times,predators,label="Wolves")
show()
