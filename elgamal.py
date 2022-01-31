import random

from params import p
from params import g
q = (p-1)/2

def keygen():   
    sk = random.randint(1,q)
    pk = pow(g,sk,p)
    return pk,sk

def encrypt(pk,m):
    r = random.randint(1,q)
    c1 = pow(g,r,p)
    c2 = pow(pow(pk,r,p)*pow(m,1,p),1,p)
    
    return [c1,c2]

def decrypt(sk,c):
    c1, c2 = c   
    
    x = pow(c1,p-1-sk,p)
    
    m = pow(c2*x,1,p)
    #m = pow(c2/cmod_inv,1,p)
    
    return m

#pk, sk = keygen()
#c = encrypt(pk, 100000000)
#print(decrypt(sk,c))
