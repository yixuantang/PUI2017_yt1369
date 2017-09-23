import sys
import requests
import json
import numpy as np

if __name__ == "__main__":
    key = sys.argv[1]
    ref = sys.argv[2]

    def geturl(key, ref):
        url1 = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="
        url2 = "&VehicleMonitoringDetailLevel=calls&LineRef="
        url = url1 + key + url2 + ref

        requrl = requests.get(url)
        return requrl.json()


    data = geturl(key, ref)
    businfo = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    busnum = np.size(businfo)

    print " Bus line : " + str(ref)
    print " Number of Active Buses : " + str(busnum)

for i in range(busnum):

    longitude = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    latitude = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']

    print " Bus " + str(i) + " is at latitude " + str(latitude) + " and longitude " + str(longitude)

