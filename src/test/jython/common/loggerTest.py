import sys

sys.path.append( "." )
sys.path.append( "./../../../main/jython" )

from common.logger import info, error, warn, debug
from net.grinder.script.Grinder import  grinder

class TestRunner:
    def __call__(self):
        info("this is info slf4j")
        error("error=%s" % (grinder.processNumber))
        warn("warn=%s" % (grinder.processNumber))
        debug("debug=%s" % (grinder.processNumber))

