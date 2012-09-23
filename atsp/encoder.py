#!/usr/bin/env python2.7
# -*- coding: utf8 -*-


class Encoder:
    pass

class LetterEncoder(Encoder):
    """
    Maps chromosomes to the symbols from the ASCII table
    with corresponding limitations, beginning with the letter 'A'
    """

    def __init__( self, ALL_GENES ):
        self.ALL_GENES = ALL_GENES

        # creates mappings for the encoding
        self.mapping = dict( enumerate( self.ALL_GENES ) )
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


