import turtle
import random
import numpy as np

# define hex Turtle
from turtle import Turtle
hex: Turtle = turtle.Turtle()

# set starting position
hex.penup()
hex.setpos(-300, 520)
hex.pendown()

# draw hexagon
hex.begin_poly()
for i in range(6):  
    hex.speed(10)
    hex.forward(600)
    hex.right(60)
hex.end_poly()

#create coordinates list
cords = hex.get_poly()

#def random point
from shapely.geometry import Polygon, Point
poly = Polygon(cords)
def random_within(poly):
    while True:
        min_x, min_y, max_x, max_y = poly.bounds
        P = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
        if poly.contains(P):
            return P

#select random point, p
P = random_within(poly)    
p = (P.x, P.y)
p1 =(P.x)
p2 =(P.x)
x = [p1]
y = [p2]

#def nearest_vertices(poly):

def get_distance(p, q):
    s_sq_difference = 0
    for pi, qi in zip(p,q):
        s_sq_difference += (pi -qi)**2
    distance = s_sq_difference**0.5
    return distance
#get distances between vertices and random point, p
d= []
for q in cords:
    d.append(get_distance(p, q))
    
#find index of adjacent vertice, m1
m1 = np.argmin(d)
#define index of adjacent vertice, m2
def m2 (d):
    m1= min(d)
    m2 = d[0]
    for i in range(len(d)):
        if m2 > d[i] and d[i]!=m1:
            m2 = d[i]
    return d.index(m2)

#Find coordinates of vertice points, nv1 and nv2   
nv1 = cords[m1]
nv2 = cords[m2(d)]
t1 = [nv1, nv2]

#set starting position to random point, p
hex.penup()
hex.setpos(p)


#Draw first Triangle
n1 = t1[0]
n2 = t1[1]
hex.begin_poly()
hex.pendown()
hex.goto(n1)
hex.goto(n2)
hex.goto(p)
hex.end_poly()
hex.penup()
T1= hex.get_poly()
T = Polygon(T1)
C= T.centroid
c = (C.x, C.y)
cx = (C.x)
cy = (C.y)
x.append(cx)
y.append(cy)
hex.setpos(c)
hex.pendown()
d1 = []
for q in cords:
    d1.append(get_distance(c, q))
    m1 = np.argmin(d1)
    a = cords[m1]
    b = cords[m2(d1)]
    g =[a, b]

#draw 10,000 triangles
def Tnext (g):
    n1 = g[0]
    n2 = g[1]
    hex.speed(500)
    hex.begin_poly()
    hex.pendown()
    x = hex.pos()
    hex.goto(n1)
    hex.goto(n2)
    hex.goto(x)
    hex.end_poly()
    hex.penup()
    t = hex.get_poly()
    T = Polygon(t)
    C= T.centroid
    c = (C.x, C.y)
    c1 =(C.x)
    c2 =(C.y)
    hex.setpos(c)
    d = []
    for q in cords:
        d.append(get_distance(c, q))
    m1 = np.argmin(d)
    a = cords[m1]
    b = cords[m2(d)]
    #TN = Triangle(n0, n1, c)
    g =[a, b, c1, c2]
    #print("This is g ;", g)
    return g

for i in range (10000):
    T = Tnext(g)
    print(i)
    x.append(T[2])
    y.append(T[3])

import matplotlib.pyplot as plt   
plt.scatter(x,y,)
plt.show()
turtle.done()

