
from random import randrange,randint


def key_gen(l):

    k=randrange(2**l,2**(l+1))
    return k


def enc(k, m):
    p=round(k**0.75)
    r=randrange(p,k-p)

    c=m*k+r
    return c


def dec(k, c):
    return c/k


