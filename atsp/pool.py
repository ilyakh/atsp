#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from random import sample, choice, randint, randrange
from util import Path
from mutation import *
from context import distance



class Child:
    def __init__( self, parents ):
        self.parents = parents

    def crossover( self ):
        f = list(self.parents[0] )
        m = list( self.parents[1] )
        child = list()

        start = randint(0, len(f)-1)
        end = randrange(start,len(f))

        child.extend( m[start:end] )
        quota = len(f) - len(child)

        for e in (set(f) - set(child)):
            child.append( e )

        if len(child) < len(f):
            for e in ( (set(f) | set(m)) - set(child) ):
                child.append(e)

        return "".join(child)



# [/] individual must take encoder as parameter to return different representations
class Individual:
    def __init__( self, chromosome ):
        self.chromosome = chromosome

    def __repr__( self ):
        return self.chromosome

class UniqueGeneIndividual(Individual):
    def __init__( self, chromosome ):
        if len( set( chromosome ) ) < len( chromosome ):
            raise Exception(
                "The Individual violates the gene uniqueness constraint"
            )
        Individual.__init__( self, chromosome )

    def to_list( self ):
        return list( self.chromosome )

class TSPIndividual(UniqueGeneIndividual):
    pass







class UniqueChromosomePool:
    def __init__( self, encoder, fitness_function, population_size=0 ):
        self.encoder = encoder
        self.fitness_function = fitness_function
        self.population_size = population_size
        #
        self.population = set() # of strings

        POSSIBLE_GENES = None

    def add( self, individual ):
        # fetches the string representation of the individual
        chromosome = individual.chromosome
        original_size = len( self )
        self.population.add( chromosome )
        # returns true if the individual was not already in the population
        return len( self.population ) > original_size

    def exclude( self, chromosome ):
        self.population = self.population.difference(
            set([chromosome])
        )

    def exclude_many( self, collection ):
        self.population = self.population.difference(
            set(collection)
        )

    def is_full( self ):
        return len( self ) == self.population_size

    def __len__( self ):
        return len( self.population )


    def populate( self ):
        while not self.is_full():
            s = sample( self.encoder.ALL_GENES, len( self.encoder.ALL_GENES ) )
            s = self.encoder.to_genotype( s )
            self.population.add( s )

    def generation( self ):
        # translate the gene to phenotypes
        phenotypes = [
            self.encoder.to_phenotype(c) for c in self.population
        ]

        # builds a ranking object that orders individuals by their fitness
        ranking = Ranking( phenotypes, self.fitness_function )

        # chooses a set of candidates for GENITOR removal
        # translates them back to genotype

        median_index = ranking.median_index()

        candidates = [
            self.encoder.to_genotype(c)
            for f,c in ranking.ranked_chromosomes[-median_index:-1]
        ]
        # [/] instead of slicing a range, just make a median value limit and
        # compare in a while loop

        # removes the least fit candidates from the population
        self.exclude_many( candidates )

        # mutates the existing worst
        # to include the children, a new rank has to be generated once more
        # ...

        

        # adds crossover children of the best elements
        # ...

        # describe the ranges of mutation and how things are stored
        # create a ranking object that





class Ranking:
    def __init__( self, population, fitness_of ):
        # creates an empty list
        self.ranked_chromosomes = []
        self.fitness_of = fitness_of

        # fills the empty list with tuples of chromosome and its fitness
        for c in population:
            self.ranked_chromosomes.append(
                ( fitness_of(c), c )
            )

        # sorts the list of tuples by the fitness of a chromosome
        # (in the previously generated tuple, the fitness has index '1')
        self.ranked_chromosomes = sorted(
            self.ranked_chromosomes, key=lambda t: t[0]
        )

    def __getitem__( self, index ):
        return self.ranked_chromosomes[index]

    def __repr__( self ):
        return "\n".join( [ c.__str__() for c,f in self.ranked_chromosomes ] )

    def normalized( self ):
        normalized_out = []
        # finds the best fitness value of the population to normalize
        # the rest against
        best_fitness = min( [f for f,c in self.ranked_chromosomes] )

        for f,c in self.ranked_chromosomes:
            normalized_out.append(
                # inverts the normalized value to fit the approximation
                ( 1.0 / (f / float(best_fitness)), c )
        )

        return normalized_out

    def __iter__( self ):
        return self.ranked_chromosomes.next()

    def median_index( self ):
        return len( self.ranked_chromosomes ) / 2

    def median_value( self ):
        pass

    def mean_value( self ):
        pass






class Pool:
    def __init__( self, population_size, fitness_function, encoder ):
        self.population = set()
        self.fitness_function = fitness_function
        self.encoder = encoder
        self.ALL_GENES = encoder.ALL_GENES
        self.population_size = population_size

    def add( self, chromosome ):
        try:
            self.population.add( chromosome )
        except Exception:
            pass

    def __len__( self ):
        return len( self.population )

    def rank( self ):
        ranking = [ (self.fitness_function(self.encoder.to_phenotype(c)), c) for c in self.population ]
        ranking = sorted( ranking, key=lambda r: r[0] )
        return ranking

    def generation( self ):
        ranking = self.rank()
        # remove the worst item

        # get the chromosome for each sex
        male = ranking[0][1]
        female = ranking[1][1]

        child = ( Child((male,female)) ).crossover()

        self.population.add(child)


        for r,c in ranking[:len(ranking)/2]:
            c = list(c)
            if choice([True,False]):
                ap = randint(0,len(c)-1)
                bp = randint(0,len(c)-1)
                a = c[ap]
                b = c[bp]
                # gene flip
                c[ap],c[bp] = c[bp], c[ap]
                # print ap,bp,c[ap],c[bp]
                self.population.add( "".join(c) )
            else:
                c.reverse()
                self.population.add( "".join(c) )

        while len(self.population) > self.population_size:
            candidates = self.rank()[len(self.rank())/2:len(self.rank())]
            self.population.remove( choice(candidates)[1] )