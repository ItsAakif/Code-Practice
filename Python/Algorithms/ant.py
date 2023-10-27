#write a code for ant colony algortihm 

import numpy as np 
import matplotlib.pyplot as plt
import random
import math

#function to calculate the distance between two cities
def distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

#function to calculate the total distance of the path
def total_distance(path):
    total = 0
    for i in range(len(path)-1):
        total += distance(cities[path[i]][0],cities[path[i]][1],cities[path[i+1]][0],cities[path[i+1]][1])
    return total


#function to calculate the probability of choosing a city
def probability(path,city,alpha,beta):
    prob = []
    for i in range(len(city)):
        if i not in path:
            prob.append((pheromone[path[-1]][i]**alpha)*(1/distance(cities[path[-1]][0],cities[path[-1]][1],cities[i][0],cities[i][1]))**beta)
        else:
            prob.append(0)
    return prob

#function to choose the next city
def next_city(path,city,alpha,beta):
    prob = probability(path,city,alpha,beta)
    return np.random.choice(city,p=prob/np.sum(prob))

#function to update the pheromone

def update_pheromone(path,city):