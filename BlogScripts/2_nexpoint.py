#Add points where x1 = x2 and y1 = y2
import libnum 

x1, y1= 15, 13 
x2, y2= 15, 13 
a, b = 0, 7 
p=17 

if (x1 == x2 and y1 == y2): 
	delta = (((3*pow(x1,2)) + a) * (libnum.invmod(2*y1, p))) % p 
else: 
	delta = ((y2-y1)*libnum.invmod(x2-x1, p)) % p 

x3 = (pow(delta,2) - x1 - x2) % p 
y3 = ((delta * (x1 - x3)) - y1) % p 

print ("\n({}, {}) + ({}, {}) = ({}, {})".format(str(x1), str(y1), str(x2), str(y2), str(x3), str(y3))) 