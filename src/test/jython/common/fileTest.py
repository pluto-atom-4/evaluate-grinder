#!/usr/bin/env jython

import sys

sys.path.append( "." )
sys.path.append( "./../../../main/jython" )

print sys.path

import common.file as FileWriter

FileWriter.writeFailure(10, "this is test")


FileWriter.writeSampling(100, "this is test", 3)
