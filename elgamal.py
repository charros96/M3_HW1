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
    c2 = pow(pow(pk,r)*m,1,p)
    return [c1,c2]

def decrypt(sk,c):
    m = pow(c[0]/pow(c[1],sk),1,p)
    return m

