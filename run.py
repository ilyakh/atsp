#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from atsp import cities, distance
from itertools import permutations
from atsp.util import Path
from random import sample, choice
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
        self.phenotypes = phenotypes
        self.population_size = population_size
        self.fitness_function = fitness_function

        # creates mappings for the encoding
        self.mapping = dict( enumerate( self.phenotypes ) )
        # maps the genotype to phenotype {A -> Bergen, ... }
        self.mapping = dict(
            [ ( chr(65 +int(k)), v ) for k,v in self.mapping.items() ]
        )
        # maps the phenotype to genotype {Bergen -> A, ... }
        self.reverse_mapping = dict(
            [ (v, k) for k,v in self.mapping.items() ]
        )

        self.population = self.initialize_population()


    def initialize_population( self ):
        population = set()

        # unpredictable time here (separate this from the algorithm run)
        while len(population) < self.population_size:
            chromosome = sample( self.mapping.keys(), len( self.phenotypes ) )
            population.add( "".join(chromosome) )

        return population


    def encode( self, phenotype ):
        return self.reverse_mapping[phenotype]

    def decode( self, genotype ):
        return self.mapping[genotype]

    def to_phenotype( self, chromosome ):
        phenotype = []
        for c in chromosome:
            phenotype.append( self.decode( c ) )
        return phenotype

    def to_chromosome( self, phenotype ):
        if phenotype is Path:
            phenotype = phenotype.path
        chromosome = []
        for g in phenotype:
            chromosome.append( self.reverse_mapping[g] )
        return chromosome

    def to_pool( self ):
        return Pool( self.population, self.fitness )

    def fitness( self, chromosome ):
        return fitness_function( self.to_phenotype(chromosome) )

class Pool:
    def __init__( self, population, fitness_function ):
        self.population = population
        self.fitness = fitness_function

    def rank( self ):
        ranking = [ (self.fitness(c), c) for c in self.population ]
        ranking = sorted( ranking, key=lambda r: r[0] )
        return ranking

    def generation( self ):
        ranking = self.rank()
        # remove the worst item
        del ranking[-1]

        male = ranking[0][1]
        female = ranking[1][1]

        child = set()
        while len(child) < len(male):
            random_gene = choice( # [!] here
            child.add(  )

        child = "".join(child)

        fresh_population = [i[1] for i in ranking]
        fresh_population.append( child )

        self.population = fresh_population

        print "New population size is: ", len( self.population )

        return child, self.fitness(child)

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

    number_of_cities = 6
    s = BruteForce( cities[:number_of_cities], repeat_cycles=1 )

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

    g = GeneticAlgorithm(
        phenotypes=cities[:6],
        population_size=10,
        fitness_function=fitness_function
    )

    # pprint( g.population )

    p = g.to_pool()

    for i in range(20):
        print p.generation()




