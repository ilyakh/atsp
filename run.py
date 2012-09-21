#!/usr/bin/env python2.7
# -*- coding: utf8 -*-


from atsp.util import Path
from atsp.context import cities, distance
from atsp.encoder import LetterEncoder
from atsp.pool import *
from itertools import permutations
from random import sample, choice, randint
from pprint import pprint
from timeit import Timer


class Solution:
    def solve( self ):
        pass

class BruteForce(Solution):
    def __init__( self, cities, repeat_cycles=1 ):
        self.solution = None
        self.candidate_paths = []

        for path in permutations( cities[:number_of_cities] ):
            self.candidate_paths.append( Path(path, distance) )

        t = Timer( lambda: self.solve() )
        time = t.timeit( number=repeat_cycles )

        print time, ": ", len(self.solution), self.solution

    def solve( self ):
        self.solution = min(
            [ p for p in self.candidate_paths ],
            key=lambda x: len(x)
        )
        return self.solution



class GeneticAlgorithm(Solution):

    def __init__( self, phenotypes, population_size, fitness_function ):
        pass






if __name__ == "__main__":

    """
    Brute Force: First, try to solve the problem by inspecting every possible
    tour. Start by writing a program to find the shortest tour among a subset of
    the cities (say, 6 of them). Measure the amount of time your program takes.
    Incrementally add more cities and observe how the time increases. What is
    the shortest tour (i.e., the actual sequence of cities, and its length)
    among the first 10 cities (that is, excluding Vinje, Fl ̊am, Sogndal, and
    Vang)? How long did your program take to find it? How long would you expect
    it to take with all 14 cities?
    """

    number_of_cities = 9
    cities = cities[:number_of_cities]

    # s = BruteForce( cities, repeat_cycles=1 )

    """
    Genetic Algorithm: Next, write a genetic algorithm (GA) to solve the problem.
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




    def fitness_function( path ):
        return len( Path( path, distance ) )

    encoder = LetterEncoder( cities )

    population_size = 200
    pool = Pool( population_size, fitness_function, encoder )




    while len(pool) < population_size:
        s = sample( cities, len(cities) )
        s = encoder.to_genotype( s )
        pool.add( s )

    # pprint( pool.population )
    # pprint( pool.rank() )

    # two best parents
    # print pool.rank()[:2]

#    counter = 0
#    while raw_input( "Continue..." ) != "n":
#        counter += 1
#        pprint( pool.population )
#        print
#        print
#        print "Best child for generation ", counter, ": ", pool.rank()[0], "\n", encoder.to_phenotype( pool.rank()[0][1] )
#        pool.generation()
#        print
#        print

    # pprint( pool.rank() )


    # Er PMX eneste passende crossover til TSP?
    # Kan jeg gi individet det laveste mulige score hvis han ikke passerer
        # alle byene (dvs. besøker samme by to ganger) ?
    # Bør fitness function være normalisert mot populasjonens beste resultat?
    # Kan man enkode individet som tegn/bokstavstrenger?
    #

    #  an element from a set; it must be a member.

    """
        Continue...
Best child for generation  831 :  (3285, 'CBHEFDGA')
['Kirkenes', 'Hammerfest', 'Troms\xf8', 'Lillehammer', 'Oslo', 'Kristiansand', 'Stavanger', 'Bergen']
set(['AGCBEDFH',
     'CBHEAGDF',
     'CBHEFAGD',
     'CBHEFDAG',
     'CBHEFDGA',
     'CBHEFGAD',
     'CBHFEAGD',
     'CBHFEDAG',
     'GACBEDFH',
     'HBCEFDGA'])


Continue...n
Ilyas-MacBook-Air:INF3490 ilyakh$ ./run.py
0.291972875595 :  3283 ('Bergen', 'Stavanger', 'Kristiansand', 'Oslo', 'Lillehammer', 'Troms\xf8', 'Hammerfest', 'Kirkenes')
Continue...
    """



    pool = UniqueChromosomePool(
        encoder=encoder,
        fitness_function=fitness_function,
        population_size=population_size
    )

    pool.populate()

    pprint( pool.rank(normalized=True) )