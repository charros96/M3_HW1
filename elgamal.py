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
    c2 = pow(pk,r,p)
    c2 = c2*m
    return [c1,c2]

def decrypt(sk,c):
    c1, c2 = c   
    c2_inv = pow(c2,-1,p)
    h = pow(c1,sk,p)
    cmod_inv = pow(h,-1,p)
    m = c2/h
    #m = pow(c2/cmod_inv,1,p)
    
    return m


