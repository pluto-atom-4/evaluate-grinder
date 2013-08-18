#!/usr/bin/env jython

import os
import sys
import random
import copy

sys.path.append( "." )
sys.path.append( "./../resources" )

import properties

#  Set full path to access test data file
dataFile = open(properties.urlListFile, "r")
lines = dataFile.readlines()
dataFile.close()

# Add sequencial number as test case number 
index = 0
seq = 101
for line in lines :
    lines[ index ] = str( seq ) + ":" + line.strip()
    index += 1
    seq +=1

def getShuffled( threadNumber, processNumber):
    global lines
    # each thread needs a local copy of the lines global list
    linesLocal = copy.copy( lines )      
    random.seed( threadNumber * processNumber )
    random.shuffle( linesLocal )        
    return linesLocal

def get():
    global lines
    # each thread needs a local copy of the lines global list
    linesLocal = copy.copy( lines )      
    return linesLocal

def item( line ):
    lineSplit = line.split(":",1)
    return {'testId':int(lineSplit[0]), 'resourcePath':lineSplit[1], 'description':description( lineSplit[1] )}

def description( resourcePath ):
    desc = resourcePath.replace( '/', '-', 1 )
    return desc
#