#!/usr/bin/env jython

import sys

sys.path.append( "." )
sys.path.append( "./../../../main/jython" )

print sys.path

import common.urls as Urls

for line in Urls.get():
    dat = Urls.item(line)
    print dat['testId'], dat['resourcePath'], dat['description']
for line in Urls.getShuffled(1, 3):
    dat = Urls.item(line)
    print dat['testId'], dat['resourcePath']
    print dat['testId'], dat['resourcePath'], dat['description']
#