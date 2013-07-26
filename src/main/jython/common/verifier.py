import sys
import string

from net.grinder.script import Statistics

sys.path.append(".")

from logger import info, error, warn, debug
from AppServerError import AppServerError

def responseTime(statistics):
    responseTime = statistics.time
    if responseTime > 5000:
        test = statistics.test
        warn( "test.number=%s test.description=%s test.time=%s" % 
                     (test.number, test.description, responseTime))
        #grinder.statistics.forLastTest.setSuccess(0)
        #writeToFile(warningLongWait)

def status(statistics):
    responseStatus = statistics.getLong("httpplugin.responseStatus")
    if responseStatus != 200 and responseStatus != 301 and responseStatus != 302 :
        test = statistics.test
        warn( "test.number=%s test.description=%s httpplugin.responseStatus=%s" % 
                     (test.number, test.description, responseStatus) )

def text(statistics, responseText):
    errMsg = "System currently unavailable"
    if string.find( responseText, errMsg ) != -1:
        test = statistics.test
        error( "test.number=%s test.description=%s responseText=%s " % 
                      (test.number, test.description, responseText) )
        raise AppServerError("test.number=%s test.description=%s message=%s " % 
                             (test.number, test.description, responseText))
#