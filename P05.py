import matplotlib.pyplot as plt 
from graphics import *
def draw_graph(V):
    x=[] 
    y=[]
    for i in V:
        x.append(i[0])
        y.append(i[1])
    plt.title("Before Appling Scan line Algorithm")
    plt.plot(x,y,c="blue",label="Polygon") 
    plt.show()
    plt.plot(x,y,c="blue",label="Polygon") 
    return max(y),min(y),max(x),min(x) 
def get_range(V):
    y2,y1,x2,x1=draw_graph(V) 
    x=[]
    y=[]
    for i in range(len(V)-1):
        x1=V[i][0] 
        y1=V[i][1]
        x2=V[i+1][0] 
        y2=V[i+1][1]
        x3,y3=calpoints(x1,y1,x2,y2,x,y)
    x=x3 
    y=y3
    for i in range(int(len(y)/2)):
        if i!= int(len(y)/2) and i!= 0:
            plt.plot([x[i],x[y.index(y[i],i+1)]],[y[i],y[i]],c="red")
    plt.title("After Appling Scan Line algorithm") 
    plt.show()
def calpoints(x1,y1,x2,y2,xlist,ylist):
    m=(y2-y1)/(x2-x1) 
    c=y1-(m*x1)
    for i in range(abs(y2-y1)*10):
        if x1<=x2:
            y=(i/10)+y1
            x=(y-c)/m
            xlist.append(x)    
            ylist.append(y)
        else:
            y=y1-(i/10)
            x=(y-c)/m
            xlist.append(x)
            ylist.append(y)
#     print(xlist,ylist)
    return xlist,ylist

count=int(input("Enter Number of vertices in a Polygon :- "))
V=[] 
print("Start entering Points :- ") 
for i in range(count):
    print("Enter Cordinates of ",i+1," Vertex :- ") 
    x,y=input().split()
    V.append((int(x),int(y)))
V.append((V[0][0],V[0][1]))
get_range(V)