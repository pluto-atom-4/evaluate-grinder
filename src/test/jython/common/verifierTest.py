import sys

from net.grinder.plugin.http import HTTPPluginControl, HTTPRequest

connectionDefaults = HTTPPluginControl.getConnectionDefaults()
""" Follow redirects (1 = true, 0 = false) """
connectionDefaults.setFollowRedirects(1)
httpUtilities = HTTPPluginControl.getHTTPUtilities()

from HTTPClient import NVPair

ffHeaders = [ NVPair('Accept', 'image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/x-shockwave-flash, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*'),
              NVPair('Accept-Language', 'en-us'),
              NVPair('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'), ]


from net.grinder.script.Grinder import grinder 
from net.grinder.script import Test

sys.path.append( "." )
sys.path.append( "./../../../main/jython" )

import common.verifier as Verifier
from common.AppServerError import AppServerError

baseUrl = "http://localhost:8000"
fullurl = "http://localhost:8080/"
fullurl2 = "http://localhost:8080/examples/servlets/servlet/HelloWorldExample"

class TestRunner:
        
    def __call__(self):
        # Define HTTP request
        httpReq = HTTPRequest( url=baseUrl, headers=ffHeaders )
        # Wrap request object with a Test object
        request = Test( 1, "This is test" ).wrap(httpReq)
        # Call GET method, run test 
        response = request.GET( fullurl )
        statistics = grinder.statistics.forLastTest
        # Verify server response time 
        Verifier.responseTime( statistics )
        # Get response status 
        Verifier.status( statistics )
        # Verify response content text
        Verifier.text( statistics, response.text )

        # set delayReports = 1 :
        # To delay the reporting before performing the test. This only
        # affects the current worker thread.        
        grinder.statistics.delayReports = 1
        httpReq2 = HTTPRequest( url=baseUrl, headers=ffHeaders )
        request2 = Test( 2, "This raise error" ).wrap(httpReq2)
        
        try: 
            # Call GET method, run test 
            response2 = request2.GET( fullurl2 )
            statistics = grinder.statistics.forLastTest
    
            Verifier.text( statistics, "System currently unavailable" )
        except AppServerError, err:
            print "Raised expected AppServerError"
            print grinder.statistics.forLastTest.test.number
            grinder.statistics.forLastTest.success = 0
            
        grinder.statistics.report()
        grinder.statistics.delayReports = 0
        response2 = request2.GET( fullurl2 )
        response2 = request2.GET( fullurl2 )
       
#
