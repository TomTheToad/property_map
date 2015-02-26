from xml.dom import minidom
 
xmldoc = minidom.parse("422.gpx")
 
trkpt = xmldoc.getElementsByTagName("trkpt")
ele = xmldoc.getElementsByTagName("ele")
 
for points in trkpt:
    lat = points.attributes['lat'].value
    lon = points.attributes['lon'].value
    for items in ele:
        alt = items.firstChild.nodeValue
    print("lat:" + str(lat) + " lon:" + str(lon) + " alt:" + str(alt) + "\n")
    


     

