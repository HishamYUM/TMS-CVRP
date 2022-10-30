import numpy as np

def nearestNeighbor(D,L):
    M=D
# Choix d'une première ville
    i=0
    j = M[i]
    road = [i]

    # Formation du chemin en KNN
    while 1:
      if len(road) == len(M):
          break
      else:
          # Distance minimale
          new_city = np.argmin(j)
          if not(new_city in road):
              road.append(new_city)
              j = M[new_city] # got to this city and find nearest neighbor
          else:
              j[new_city] = np.inf

    # Ajout du dernier noeud pour terminer le tour
    road.append(i)
    road = np.array(road) + 1
    
    S=[]
    for i in range(len(road)):
        S.append(L[road[i]-1])
    print(S)
    return S