from tinyec.ec import SubGroup, Curve 
import hashlib 
import libnum 
  
hashval = 123111 #Assumed that this is a hash of some custom text message 
  
field = SubGroup(17, g=(15, 13), n=18, h=1) 
curve = Curve(a=0, b=7, field=field, name='NonceReuseDemo') 
print ("\nG :=> ({},{})".format(str(15), str(13))) 
privateKey = 10 
print ("\nPrivte Key :=> " + str(privateKey)) 
publicKey = privateKey * curve.g 
print ("\nPublic Key :=> PrivateKey * G :=> 10 * G :=> ({},{})".format(str(publicKey.x), str(publicKey.y))) 
  
k = 7  
print ("\nk (Nonce) :=> " + str(k)) 
R = (k*curve.g) #Temp Variable 
print ("\nk * G :=> 7 * G :=> ({},{})".format(str(R.x), str(R.y))) 
r = R.x 
print ("\nr is x co-ordinate of (k * G) :==> " + str(r)) 
  
s = (libnum.invmod(k, curve.field.n) * (hashval + r * privateKey)) % curve.field.n 
print ("\ns :=> k\u207b\u00b9 * (H(M) + r * PrivateKey) :=> " + str(s)) 
print ("\nSignature of Msg :==> ({},{})".format(str(r), str(s))) 