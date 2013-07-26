#!/usr/bin/ksh
GRINDERPATH=/home/$USER/lib/grinder-3.11
GRINDERPROPERTIES=/home/$USER/workspace/grinder/resources/grinder.properties
CLASSPATH=$GRINDERPATH/lib/grinder.jar:$CLASSPATH
JAVA_HOME=$USER/lib/jdk1.6.0_24
PATH=$JAVA_HOME/bin:$PATH
