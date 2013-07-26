#!/usr/bin/ksh
. /home/$USER/workspace/grinder/bin/setGrinderEnv.sh
java -classpath $CLASSPATH net.grinder.TCPProxy -console -http > /home/$USER/workspace/grinder/proxy-generated-scripts/grinder-`date +%m-%d-%Y%z-%S`.py
