#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from random import sample, choice, randint, randrange
from encoder import LetterEncoder



class Child:
    def __init__( self, parents ):
        self.parents = parents

    def crossover( self ):
        f = list(self.parents[0])
        m = list(self.parents[1])

        print randrange( m )


class Pool:
    def __init__( self, fitness_function, encoder ):
        self.population = set()
        self.fitness_function = fitness_function
        self.encoder = encoder

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
        del ranking[-1]

        # get the chromosome for each sex
        male = ranking[0][1]
        female = ranking[1][1]

        # slice the chromosomes
        male_part = male[:len(male)/2+1]
        female_part = female[len(male)/2:-1]

        # do a random mutation on a reoccuring element

        print female_part, male_part

        # combine the chromosomes into a child
        # child = male_part + female_part

        child = []

        # [!] give up

        child = "".join(child)


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

        print "New population size is: ", len( self.population )

        return child, self.fitness(child)