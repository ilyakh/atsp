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
        return len( self.population ) == self.population_size

    def __len__( self ):
        return len( self.population )

    def generation( self ):
        ranking = self.rank()
        candidates = [c for i,c,f in ranking[-len(ranking)/2:-1]]
        self.exclude_many( candidates )

        # describe the ranges of mutation and how things are stored
        # create a ranking object that 



    def rank( self, normalized=False ):

        out = []
        best_fitness = None

        for chromosome in self.population:
            individual = TSPIndividual( chromosome )
            fitness = self.fitness_function(
                self.encoder.to_phenotype(chromosome)
            )
            out.append(
                ( TSPIndividual(chromosome), chromosome, fitness )
            )

        if normalized:
            normalized_out = []
            best_fitness = min( [f for i,c,f in out] )

            for i,c,f in out:
                normalized_out.append(
                    # inverts the normalized value to fit the approximation
                    ( i, i.chromosome, 1.0 / (f / float(best_fitness)) )
            )
            out = normalized_out

        return sorted( out, key=lambda x: x[1] )


    def populate( self ):
        while not self.is_full():
            s = sample( self.encoder.phenotypes, len( self.encoder.phenotypes ) )
            s = self.encoder.to_genotype( s )
            self.population.add( s )


















class Pool:
    def __init__( self, population_size, fitness_function, encoder ):
        self.population = set()
        self.fitness_function = fitness_function
        self.encoder = encoder
        self.phenotypes = encoder.phenotypes
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



        # slice the chromosomes
#        male_part = male[:len(male)/2+1]
#        female_part = female[len(male)/2:-1]

        # do a random mutation on a reoccuring element

#        print female_part, male_part

        # combine the chromosomes into a child
        # child = male_part + female_part
#
#        child = []

        # [!] give up
#
#        child = "".join(child)


        # mutate on the basis of rank

#        def mutate( chromosome ):
#            mutant = list(chromosome)
#            mutant[randint(0, len(chromosome))-1] = choice(list(self.genes))
#            return mutant
#
#        fresh_population = []
#
#        for k,v in ranking:
#            a = v
#            for i in range(k):
#                a = mutate(a)
#            fresh_population.append( a )

#        print "New population size is: ", len( self.population )

#        return child, self.fitness(child)