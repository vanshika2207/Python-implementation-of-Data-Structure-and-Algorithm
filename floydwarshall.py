def printsolution(noofvertices,distance):
    for i in range(noofvertices):
        for j in range(noofvertices):
            if (distance[i][j]=="inf"):
                print('INF',end='')
            else:
                print(distance[i][j],end='')
        print(" ")

def floydwarshall(noofvertices,G):
    distance=G
    for k in range(noofvertices):
        for i in range(noofvertices):
            for j in range(noofvertices):
                distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])
    printsolution(noofvertices,distance)