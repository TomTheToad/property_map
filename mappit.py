from xml.dom import minidom
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
 
xmldoc = minidom.parse("422.gpx")
 
trkpt = xmldoc.getElementsByTagName("trkpt")
ele = xmldoc.getElementsByTagName("ele")
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

count = 0

for points in trkpt:
    lat = points.attributes['lat'].value
    lon = points.attributes['lon'].value
    alt = ele[count].firstChild.nodeValue
    count += 1

    ax.scatter(float(lat), float(alt), float(lon))
    
ax.set_xlabel('latitude')
ax.set_ylabel('altitude')
ax.set_zlabel('longitude')
    
plt.show()