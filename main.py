import sys, os, re, time
from lib import *

def init():
    file_path = "lib"
    path = os.path.abspath(file_path)
    os.environ['PYDFHOME'] = path

def siteDomainFilter(domain):
    pattern = "uol.com.br$"
    for d in domain:
        match = re.search(pattern, d)
        if match:
            return d
    return "" 

def printDomain(domain):
    if len(domain[0])>0:
        print domain[0]
   
def pipeLine(processors,filename):
    graph = DFGraph()
    nprocs = int(processors)
    try:
        fp = open(filename, "r")
    except Exception as e:
        print("File exception occorring:",e)
        exit

    scheduler = Scheduler(graph, nprocs, mpi_enabled = False)

    source = Source(fp)
    graph.add(source)

    filtred = FilterTagged(siteDomainFilter, 1)
    graph.add(filtred)

    serialized = Serializer(printDomain, 1)
    graph.add(serialized)

    source.add_edge(filtred, 0)
    filtred.add_edge(serialized, 0)

    start_time = time.time()
    scheduler.start()
    stop_time = time.time()
    print "Execution time %.3f" %(stop_time-start_time)

if __name__ == '__main__':
    init()
    if len(sys.argv) > 2:
        pipeLine(sys.argv[1],sys.argv[2])
    else:
        if sys.argv[1] == "" and sys.argv[2] == "":
            print("You forget the processor number and file name")
        elif sys.argv[1] == "":
            print("You forget the processor number")
        else:
            print("You forget the file name")













