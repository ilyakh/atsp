#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

import pickle
import pprint
from itertools import permutations
from timeit import timeit
from random import sample


def calculate_distance( path, distance ):
    return sum( [ distance[step[0]][step[1]] for step in steps(path) ] )

class Solution:
    def __init__( self, data ):
        pass
    def __call__( self ):
        """ run the solution """
        pass

if __name__ == "__main__":
    cities, distance = get_distances_from_file( "citiesAndDistances.txt" )


    """
    Brute Force First, try to solve the problem by inspecting every possible
    tour. Start by writing a program to find the shortest tour among a subset of
    the cities (say, 6 of them). Measure the amount of time your program takes.
    Incrementally add more cities and observe how the time increases. What is
    the shortest tour (i.e., the actual sequence of cities, and its length)
    among the first 10 cities (that is, excluding Vinje, Fl ̊am, Sogndal, and
    Vang)? How long did your program take to find it? How long would you expect
    it to take with all 14 cities?
    """

    brute_force_paths = permutations( cities[0:5] )

    candidate_paths = []
    for path in brute_force_paths:
        candidate_paths.append( (calculate_distance(path, distance), path) )

    pprint.pprint(
        sorted(candidate_paths, key=lambda x: x[0], reverse=True )
    )


    """
    Genetic Algorithm Next, write a genetic algorithm (GA) to solve the problem.
    Choose mutation and crossover operators that are appropriate for the problem
    (see chapter 3 of the Eigen and Smith textbook). Choose three different
    values for the population size. Define and tune other parameters yourself
    and make assumptions as necessary (and report them, of course).
    For all 14 cities: Report the average and the best tour length of 5 runs of
    the algorithm for each of the different population sizes you have chosen;
    conclude which is best in terms of tour length and number of generations of
    evolution time. Plot the average and the best tour length as a function of
    the number of generations of evolution for each population size, for one run.
    Among the first 10 cities, did your GA find the shortest tour (as found by
    brute force)? Did it come close? For both 10 and 14 cities: How did the
    running time of your GA compare to that of your brute force algorithm? How
    many tours were inspected by your GA as compared to by your brute force
    algorithm?
    """


    # to create a population I use the sample method in combination with
    # the permutations I've also used for the brute force approach.

    # use integers to represent cities

    # instead of sampling the permutations set, make an empty set
    # and fill it until it is of a proper size

    # replace the bad individuals by leaving the successful parents alive

    population = []
    city_permutations = permutations(cities)
    for i in xrange( 0,6 ):
        population.append( city_permutations.next() )

    for ind in population:
        print ind[0], ind[-1], ": ", calculate_distance(ind, distance)