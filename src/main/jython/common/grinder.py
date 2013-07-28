############################################################################################
# Script: grinder.py
############################################################################################

import sys

from net.grinder.script.Grinder import grinder 
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPPluginControl, HTTPRequest
 
sys.path.append(".")

from AppServerError import AppServerError
from sampling import sampling
import connection
import logger as Logger
import properties
import urls as Urls 
import verifier as Verifier

connectionDefaults = HTTPPluginControl.getConnectionDefaults()
""" Follow redirects (1 = true, 0 = false) """
connectionDefaults.setFollowRedirects(1)

httpUtilities = HTTPPluginControl.getHTTPUtilities()

#####################################################################################

class TestRunner:
    def __call__(self):
        # for-loop through the lines in the file
        for line in Urls.getShuffled( grinder.processNumber, grinder.threadNumber ):
            dat = Urls.item( line )
            testId = dat[ 'testId' ]
            resourcePath = dat[ 'resourcePath' ]
            fullurl =  properties.baseUrl + resourcePath
            desc = fullurl.replace( 'http://', '', 1 ) 
            try: 
                # Delay the statics return by 1 second to check for success
                grinder.statistics.delayReports = 1
                # Define HTTP request
                httpReq = HTTPRequest( url=properties.baseUrl, headers=connection.headers )
                # Wrap request object with a Test object
                request = Test( testId, desc ).wrap( httpReq )
                # Call GET method, run test 
                response = request.GET( fullurl )
                statistics = grinder.statistics.forLastTest
                # Verify server response time 
                Verifier.responseTime( statistics )
                # Get response status 
                Verifier.status( statistics )
                # Verify response content text
                Verifier.text( statistics, response.text )
                # Sampling...
                sampling( grinder.runNumber, response.text )

            except ValueError, err:
                Logger.error( err )
                
            except AppServerError, err:
                break
        # end for-loop
# end TestRunner