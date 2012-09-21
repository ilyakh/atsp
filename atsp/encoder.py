#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 


class Encoder:
    pass

class LetterEncoder(Encoder):
    """
    Maps chromosomes to the alphabet
    """

    def __init__( self, phenotypes ):
        self.phenotypes = phenotypes

        # creates mappings for the encoding
        self.mapping = dict( enumerate( self.phenotypes ) )
        # maps the genotype to phenotype {A -> Bergen, ... }
        self.mapping = dict(
            [ ( chr(65 + int(k)), v ) for k,v in self.mapping.items() ]
        )
        # maps the phenotype to genotype {Bergen -> A, ... }
        self.inverse_mapping = dict(
            [ (v, k) for k,v in self.mapping.items() ]
        )

    def encode( self, phenotype ):
        return self.inverse_mapping[phenotype]

    def decode( self, genotype ):
        return self.mapping[genotype]

    def to_genotype( self, phenotype_set ):
        genotype = [ self.encode(g) for g in phenotype_set ]
        return "".join( genotype )

    def to_phenotype( self, genotype_set ):
        phenotype = [ self.decode(g) for g in genotype_set ]
        return phenotype


