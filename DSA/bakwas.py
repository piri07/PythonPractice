#add operator 
class point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0} {1})".format(self.x,self.y)

    def __mul__(self,other):
        x= self.x*other.x
        y=self.y*other.y
        return point(x,y)
    

p1=point(3,54)
p2=point(5,6)
print(p1*p2)


#magintude of point comparison

class Point:
    def __init__(self,x,y):
        self.x =x 
        self.y = y

    def __str__(self):
        return "({0} {1})".format(self.x,self.y)

    def __lt__(self,other):
        #lt = less than
        self_mag = (self.x**2 + self.y**2)**0.5
        other_mag = (other.x**2 + other.y**2)**0.5
        return self_mag>other_mag
        #it is a boolean expression which return true or false


P1 = Point(1,1)
P2 = Point(-2,-3)
P3 = Point(1,-1)

print(P1<P2)
print(P2<P3)
print(P1<P3)




