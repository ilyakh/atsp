#!/usr/bin/env python2.7
# -*- coding: utf8 -*-



__all__ = [
    'Path'
]



class Path:
    def __init__( self, path, distance_table ):
        self.path = path
        self.distance = distance_table

    def steps( self ):
        steps = []
        for i in xrange( len(self.path) -1 ):
            steps.append( (self.path[i], self.path[i+1]) )
        return steps

    def __len__( self ):
        cummulative_distance = 0
        for step in self.steps():
            cummulative_distance += self.distance[step[0]][step[1]]
        return cummulative_distance

    def __repr__( self ):
        return "%s: %s" % (len(self), self.path.__str__())

    def __str__( self ):
        return self.path.__str__()

    def __cmp__( self, other ):
        if len( self ) > len( other ):
            return 1
        elif len( self ) == len ( other ):
            return 0
        else:
            return -1
