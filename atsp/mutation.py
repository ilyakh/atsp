#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

from random import randrange, choice

def random_selector( locus=None ):
    return choice( [True, False] )

def unique_mutator( locus, chromosome, all_genes ):
    out = locus
    available_genes = set( all_genes ) - set( chromosome )

    # if there are available genes, mutates, otherwise falls back on the
    # supplied preexisting gene
    if len( available_genes ):
        out = choice( available_genes )

    return out



class Filter:
    """
    'selector' is a function that decides whether a gene should
    be mutated or not.
    'mutator' is a function that decides how a gene should be
    mutated, and defines a pool from which the mutation gene
    shoul be fetched.
    """
    def __init__( self, selector, mutator ):
        self.selector = selector
        self.mutator = mutator


class UniqueGeneFilter( Filter ):

    def __init__( self, selector ):
        Filter.__init__( self, selector=selector, mutator=unique_mutator )

    def __call__( self, chromosome ):
        mutant = []

        for locus in list( chromosome ):
            if self.selector():
                # assigns a random gene from the available pool
                mutant.append( self.mutator( locus, chromosome ) )
            else:
                # assigns the unchanged value
                mutant.append( locus )

        print mutant
        return mutant
