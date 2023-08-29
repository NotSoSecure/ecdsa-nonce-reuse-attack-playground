from tinyec.ec import SubGroup, Curve 
import hashlib 
import libnum 
  
hashval = 103318048148376957923607078689899464500752411597387986125144636642406244063093 
#hashval = 123423418048148376989543525467878689899464500752234234234243234144636642406244 
print ("\nHash of Message") 
print (hashval) 
  
field = SubGroup(2 ** 256 - 2 ** 32 - 2 ** 9 - 2 ** 8 - 2 ** 7 - 2 ** 6 - 2 ** 4 - 1, g=(108607064596551879580190606910245687803607295064141551927605737287325610911759, 6661302038839728943522144359728938428925407345457796456954441906546235843221), n=115792089237316195423570985008687907852837564279074904382605163141518161494337, h=1) 
curve = Curve(a=0, b=7, field=field, name='NonceReuseDemo') 
  
privateKey = 112757557418114203588093402336452206775565751179231977388358956335153294300646 
publicKey = privateKey * curve.g 
print ("\nPrivate Key") 
print (privateKey) 
print ("\nPublic Key co-ordinate") 
print ("({},{})".format(str(publicKey.x), str(publicKey.y))) 
  
k = 10  
R = (k*curve.g) #Temp Variable 
print ("\nk * G") 
print ("({},{})".format(str(R.x), str(R.y))) 
r = R.x 
print ("\nr is x co-ordinate of (k * G)") 
print (str(r)) 
  
s = (libnum.invmod(k, curve.field.n) * (hashval + r * privateKey)) % curve.field.n 
print ("\ns :=> k\u207b\u00b9 * (H(M) + r * PrivateKey)") 
print (str(s)) 
print ("\nSignature of Msg (r,s)") 
print ("({},{})".format(str(r), str(s))) 
  
print ("\n\nVerification") 
s1 = libnum.invmod(s, curve.field.n) 
R = ((hashval * s1) * curve.g) + ((r * s1) * publicKey) 
print ("r'") 
print (R.x) 