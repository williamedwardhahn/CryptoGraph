import urllib2

print "Graph test 1" 
response = urllib2.urlopen('http://www.cryptocoincharts.info/v2/api/listCoins')
html = response.read()

currentNodeList = html

print(type(html))


A=(currentNodeList.split("{"))

print type(A)


print A[0]
print A[1]
print A[2]



B=A[1].split("\"")


print B[0]
print B[1]
print B[2]
print B[3]
print B[4]
print B[5]
print B[6]
print B[7]
print B[8]
print B[9]
print B[10]
print B[11]
print B[12]
print B[13]
print B[14]
print B[15]
print B[16]
print B[17]
print B[18]
print B[19]
print B[20]