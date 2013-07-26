#!/usr/bin/ksh
. /home/$USER/workspace/grinder/bin/setGrinderEnv.sh
java -classpath $CLASSPATH net.grinder.Grinder $GRINDERPROPERTIES
