import random

from params import p
from params import g
q = (p-1)/2

def keygen():   
    sk = random.randrange(1,q)
    pk = pow(g,sk,p)
    return pk,sk

def encrypt(pk,m):
    r = random.randrange(1,q)
    c1 = pow(g,r,p)
    c2 = pow(pk,r,p)
    c2 = pow(c2*m,1,p)
    return [c1,c2]

def decrypt(sk,c):
    num = pow(c[1],1,p)
    den = pow(c[0],-sk,p)
    m=num*den
    return m

pk,sk = keygen()
c = encrypt(pk,1010)
print(decrypt(sk,c))