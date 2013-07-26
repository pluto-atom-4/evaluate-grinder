import sys

sys.path.append(".")

import properties

import file as FileWriter

sampleCount = 0

def sampling( runNumber, responseText ):
    global sampleCount
    if properties.sampleRate :
        if  runNumber % properties.sampleRate == 0:
            FileWriter.writeSampling(runNumber, responseText, sampleCount)
            sampleCount += 1

