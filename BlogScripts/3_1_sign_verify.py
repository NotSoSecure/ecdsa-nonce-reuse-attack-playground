from tinyec.ec import SubGroup, Curve  
import hashlib  
import libnum  
  
field = SubGroup(17, g=(15, 13), n=18, h=1)  
curve = Curve(a=0, b=7, field=field, name='NonceReuseDemo')  
  
  
print ("\nVerification")  
hashval = 123111  
r = 10 
print ("r :=> " + str(r))  
s = 13 
privateKey = 10 
publicKey = privateKey * curve.g 
s1 = libnum.invmod(s, curve.field.n)  
R = ((hashval * s1) * curve.g) + ((r * s1) * publicKey)  
print ("r' :=> " + str(R.x)) 