#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from random import sample, choice, randint, randrange
from encoder import LetterEncoder



ENCODER = None



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
    pass

class UniqueGeneIndividual(Individual):
    def __init__( self, chromosome ):
        self.chromosome = chromosome

    def mutate( self, selector_function ):
        """
        The safe default mutation that only swaps the positions of
        loci in the chromosome.
        """

        chromosome = self.to_list()

        if selector_function is None:
            # assigns a default selector function
            pass

        for locus in chromosome:




    def to_list( self ):
        return list( self.chromosome )

    def get_candidate_genes( self ):
        """
        Collects the non-existing genes for this individual.
        Used to mutate the chromosome while maintaining the
        gene-uniqueness constraint.
        """
        return list(
            set( ENCODER.GENES ) - set( self.to_list() )
        )



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