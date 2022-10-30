import requests
import urllib.parse
import urllib.request
import json
import pandas as pd
import requests



def coordToDist(table):
    bingMapsKey = "Ajm_tY6mR2Pru3-rf4qr1aeQx0_h6Ttah_EaS1quWJyCwXCvdpKHCtxYOQH9ddqj"
    routeUrl = "https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?key=" + bingMapsKey
    origins=[]
    destinations=[]
    size=len(table)
    for i in range(size):
        origins.append(table.iloc[i].to_dict())

        destinations.append(table.iloc[i].to_dict())

    restfull={"origins":origins,"destinations":destinations,"travelMode": "driving"}


    response = requests.post(routeUrl, data=json.dumps(restfull))
    results=response.json()
    dist_mat = [[0]*size for i in range(size)]
    L=[]
    i=0
    j=0
    for l in range(size * size):
        distance = results["resourceSets"][0]["resources"][0]["results"][l]["travelDistance"]
        L.append(distance)

    for i in range(size):
        for j in range(size):
            dist_mat[i][j] = L[(i*size)+j]
    return dist_mat


def namesToDist(liste):
    M=[[0]*3 for i in range(len(liste))]
    for i in range(len(liste)):
        url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(liste[i]) +'?format=json'
        response = requests.get(url).json()
        M[i][0]=liste[i]
        M[i][1]=response[0]["lat"]
        M[i][2]=response[0]["lon"]
    df=pd.DataFrame(M)
    df.columns=['villes','latitude','longitude']
    return (coordToDist(df))