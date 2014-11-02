#!/usr/bin/python

import math
import random

for i in range(10):
    x = 9*random.random()
    y = pow(x+random.gauss(0,0.3),2)
    print x,y

