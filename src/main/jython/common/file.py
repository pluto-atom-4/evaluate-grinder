import uuid

#####################################################################################
        # Utility method that writes the given string to a uniquely named file using a FilenameFactory
def writeFailure(runNumber, text):
    filename = ("grinder_failure-%05d-%s.txt" % (runNumber, uuid.uuid4()))
    print filename
    outFile = open(filename, "a")
    print >> outFile, text
    outFile.close()

def writeSampling(runNumber, text, sampleCount):
    print "Writing Sample", str(sampleCount)
    filename = ("grinder_sampling-%05d-%05d-%s.txt" % (sampleCount, runNumber, uuid.uuid4()))
    print filename
    outFile = open(filename, "a")
    print >> outFile, text
    outFile.close()