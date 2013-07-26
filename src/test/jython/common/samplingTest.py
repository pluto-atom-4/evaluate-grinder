#!/usr/bin/env jython

import sys

sys.path.append( "." )
sys.path.append( "./../../../main/jython" )

print sys.path

import common.file as FileWriter
from common.sampling import sampling

sampling(50, "SamplingTest..")