from xml.dom import minidom
 
xmldoc = minidom.parse("422.gpx")
 
trkpt = xmldoc.getElementsByTagName("trkpt")
ele = xmldoc.getElementsByTagName("ele")
 
count = 0

for points in trkpt:
    lat = points.attributes['lat'].value
    lon = points.attributes['lon'].value
    alt = ele[count].firstChild.nodeValue
    count += 1
    print("lat:" + str(lat) + " lon:" + str(lon) + " alt:" + str(alt) + "\n")
    


     

