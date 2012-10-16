"""test de python "http://www.python.org/index.html"  """
import httplib
import sys
import pdb
LOG = False
if(len(sys.argv) > 2):
    LOG = True


def logger(filelocal, message):
    """logger"""
    if LOG:
        filelocal.write(message)


def connect(adresse):
    """connect"""
    pdb.set_trace()
    conn = httplib.HTTPConnection("cache.univ-st-etienne.fr", 3128)
    conn.request("GET", adresse)
    reponse = conn.getresponse()
    return reponse
    #print r1.status,r1.reason
    #data=r1.read()
    #print len(data)
    #print len(data.split(" "))

MYCONNECT = connect(sys.argv[1])
MYFILE = open(sys.argv[2], "w")
logger(MYFILE, "status:%s\n"%str(MYCONNECT.status))
DATA=MYCONNECT.read()
logger(MYFILE, "longeur:%d\n"%len(DATA))
logger(MYFILE, "mots:%d\n"%len(DATA.split(" ")))
MYFILE.close()
