import json
from django.shortcuts import render
from utilities.distances import namesToDist
from utilities.knn import nearestNeighbor
from utilities.b_b import BranchandBound
from utilities.c_w import clarke_and_wright
import pandas as pd

# Create your views here.
def importation(request):
    if request.method == 'POST':
        file = request.FILES["myfile"]
        csv = pd.read_csv(file)
        cities=csv["cities"].tolist()
        DistMatrix = namesToDist(cities)
        valeurselectionnee = request.POST["methode"]
        if valeurselectionnee == 'KNN':
            solution = nearestNeighbor(DistMatrix,cities)
        elif valeurselectionnee == 'Branch and Bound':
            solution = BranchandBound(DistMatrix,cities)
        elif valeurselectionnee == 'Clarke and Wright':
            solution = clarke_and_wright(DistMatrix,cities)

        json_list = json.dumps(solution)
        context = {"cities": cities, "solution": solution, "valeurselectionnee": valeurselectionnee, "json_list": json_list}
        

        return render(request,"index.html",context)
    else:
        return render(request, 'index.html')






