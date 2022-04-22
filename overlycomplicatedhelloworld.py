import itertools
# the overly complicated hello world works by 
# first creating the prime factorization of the unicode keys of
# every character in hello world, 
# multiplying out, 
# then printing by value. 

class Pair:
    def __init__(self, val1, val2): 
        self.val1 = val1
        self.val2 = val2

class PrimeFactorization:
    def __init__(self, *pairs):
        self.factor_exponent_pairs: list[Pair] = []
        for pair in pairs: 
            self.factor_exponent_pairs.append(pair)

    def value(self): 
        val = 1
        for pair in self.factor_exponent_pairs: 
            val *= (pair.val1**pair.val2)
        return val

# convenience method 
def pairOf(i, j): 
    return Pair(i, j)

# here we go! 

H = PrimeFactorization(
        pairOf(2, 3),
        pairOf(3, 2))
e =  PrimeFactorization(pairOf(101, 1))
l =  PrimeFactorization(
        pairOf(2, 2),
        pairOf(3, 3))
o = PrimeFactorization(
        pairOf(3, 1),
        pairOf(37, 1))

W = PrimeFactorization(
        pairOf(7, 1),
        pairOf(17, 1))
r = PrimeFactorization(
        pairOf(2, 1),
        pairOf(3, 1),
        pairOf(19, 1))
d = PrimeFactorization(
        pairOf(2, 2),
        pairOf(5, 2))

print(chr(H.value()), end="")
print(chr(e.value()), end="")
print(chr(l.value()), end="")
print(chr(l.value()), end="")
print(chr(o.value()), end=" ")
print(chr(W.value()), end="")
print(chr(o.value()), end="")
print(chr(r.value()), end="")
print(chr(l.value()), end="")
print(chr(d.value()), end="")
print(chr(0))