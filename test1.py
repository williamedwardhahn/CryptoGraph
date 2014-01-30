import urllib2

print "Graph test 1" 
response = urllib2.urlopen('http://www.cryptocoincharts.info/v2/api/listCoins')
html = response.read()

print html
