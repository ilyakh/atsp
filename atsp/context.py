#!/usr/bin/env python2.7
# -*- coding: utf8 -*- 

import pickle

class Context:
    cities = []
    distance = {}


class PickleContext(Context):
    def __init__( self, source_path ):
        pass


class TextContext(Context):
    def __init__( self, source_path ):
        with open( source_path, 'r' ) as source:
            data = source.read()
            table = ([ i.split( "\t" ) for i in data.split( "\n" ) ])[1:-1]
            cities = [ line[0] for line in table ]

            distance_table = {}
            for line in table:
                distance_table[line[0]] = {}
                for city, distance in zip( cities, line[1:] ):
                    distance_table[line[0]][city] = int(distance)

        self.distance = distance_table
        self.cities = cities



# initializes the context for the distance/city data
default_context = TextContext( "data/citiesAndDistances.txt" )

# assigns the distance/city data to importable variables
cities = default_context.cities
distance = default_context.distance