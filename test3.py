import urllib2 as URL
import json as JS
 
coinlist = URL.urlopen('http://www.cryptocoincharts.info/v2/api/listCoins')
toptenpairs = URL.urlopen('http://www.cryptocoincharts.info/v2/api/tradingPairs')

rawnodelist = coinlist.read()
nodelist = JS.loads(rawnodelist)

rawtoptenpairs = toptenpairs.read()
toptenpairslist = JS.loads(rawtoptenpairs)

def getidlist():
    idlist = []
    for i in range(len(nodelist)):
        idlist.append(nodelist[i]['id'])
    return idlist

def gettoptenpairsidlist():
    toptenpairsidlist = []
    for i in range(len(toptenpairslist)):
        toptenpairsidlist.append(toptenpairslist[i]['id'])
    return toptenpairsidlist    
    
    


ids = getidlist()
pairsids = gettoptenpairsidlist()

print ids
print pairsids


