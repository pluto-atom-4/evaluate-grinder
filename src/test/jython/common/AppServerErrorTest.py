import sys

sys.path.append(".")
sys.path.append("../common")
sys.path.append( "./../../../main/jython" )

from common.AppServerError import AppServerError

raise AppServerError("test.description=%s message=%s " % ("this is test", "dummy error messeage"))
