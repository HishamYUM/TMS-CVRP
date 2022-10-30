import numpy as np
import pandas as pd


def clarke_and_wright(dist_matrix, cities):

    j=0
    for i in dist_matrix: 
        i.insert(0, cities[j])
        j+=1
    dist_matrix.insert(0, cities)
    # print(dist_matrix)

    size = len(dist_matrix) -1
    economies = [[0 for i in range(size)] for j in range(size)]
    for i in range(1, size+1):
        for j in range(1,size+1):
            economies[i-1][j-1] = dist_matrix[i][1] + dist_matrix[1][j] - dist_matrix[i][j]
    
    #Calculate economies
    for i in range(1, len(economies)):
        for j in range(1, len(economies)): 
            if((i==j) or (economies[i][j]==economies[j][i])):
                economies[j][i]=0

    


    T = [1,1]

    # w, h = size, size
    mat_null = [[0] * size for i in range(size)]

    for i in range(1, len(economies)):
        for j in range(1,len(economies)):   
            if((economies[i][j]==np.max(economies))):
                if ((i+1 not in T) & (j+1 not in T)): 
                    T.insert(1,i+1)
                    T.insert(2,j+1)
                    economies[i][j]=0
                    break

    while economies != mat_null:
        for i in range(1,len(economies)):
            for j in range(1,len(economies)):   
                if((economies[i][j]==np.max(economies))):
                
                    if ((i+1 in T) & (j+1 in T)): 
                        economies[i][j]=0 
                    elif ((i+1 not in T) & (j+1 not in T)): 
                        economies[i][j]=0 
                    elif((i+1==T[1]) & (j+1 not in T)):
                        T.insert(1,j+1)
                        economies[i][j]=0 
                    elif((i+1==T[len(T)-2]) & (j+1 not in T)):
                        T.insert(len(T)-1,j+1) 
                        economies[i][j]=0
                    elif((j+1==T[1]) & (i+1 not in T)):
                        T.insert(1,i+1)
                        economies[i][j]=0 
                    elif((j+1==T[len(T)-2]) & (i+1 not in T)):
                        T.insert(len(T)-1,i+1) 
                        economies[i][j]=0 
                    else:
                        economies[i][j]=0  


    route = []

    for i in range(len(T)):
        route.insert(i, dist_matrix[T[i]][0])

    return route


