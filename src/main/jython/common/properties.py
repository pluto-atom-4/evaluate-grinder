import sys
import os

sys.path.append(".")
sys.path.append("./../common")

# Get current directory path
directory = os.path.join( sys.path[0], sys.argv[0] )

# User defined parameters(s)
# Get parameters
baseUrl = os.getenv( 'urlListFile', "http://localhost:8080" )
print ("baseUrl=%s" % baseUrl)
#
baseSSLUrl = os.getenv( 'baseSSLUrl', "https://localhost:8080" )
print ("baseSSLUrl=%s" % baseSSLUrl)
#
sampleRate = int(os.getenv( 'sampleRate', "50" ))
print ("sampleRate=%d" % sampleRate)
#
rampUpInterval = int(os.getenv( 'rampUpInterval', "30" ))
print ("rampUpInterval=%d" % rampUpInterval)
# ./../../../main/jython
urlListFile = os.getenv( 'urlListFile', os.path.join( '.', '..', '..', '..','resources', 'grinder-testdata.txt' ) )
print ("urlListFile=%s" % urlListFile)
#
resourceDir = os.getenv( 'resourceDir', os.path.join( '.', '..', '..', '..','resources' ) )
print ("resourceDir=%s" % resourceDir)
#
followRedirects = os.getenv( 'followRedirects', 'false' )
print ("followRedirects=%s" % followRedirects)
