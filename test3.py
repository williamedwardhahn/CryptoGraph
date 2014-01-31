import urllib2 as URL
import json as JS
 
coinlist = URL.urlopen('http://www.cryptocoincharts.info/v2/api/listCoins')

rawnodelist = coinlist.read()

nodelist = JS.loads(rawnodelist)

def getidlist():
    global idlist
    idlist = []
    for i in range(len(nodelist)):
        idlist.append(nodelist[i]['id'])

getidlist()

print idlist


