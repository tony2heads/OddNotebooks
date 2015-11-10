#!/usr/bin/env python

import sys
import math

def isqrt(n):
   return int(math.floor(math.sqrt(float(n))))

def factorize(n):
   if n < -1: return [[-1, 1]] + factorize(-n)
   elif n == -1: return [[-1, 1]]
   elif n == 0: return [[0, 1]]
   elif n == 1: return [[1, 1]]
   else:
      factors = []
      divisor = 2
      while divisor <= isqrt(n):
         power = 0
         while (n % divisor) == 0:
            n //= divisor
            power += 1
         if power > 0:
            factors.append([divisor, power])
         divisor += 1
      if n > 1:
         factors.append([n, 1])
      return factors

def divisorsFromFactors(factors):
   if not factors: return [1]
   else:
      base = factors[0][0]
      if base == -1: return divisorsFromFactors(factors[1:])
      elif base == 0: return []
      elif base == 1: return divisorsFromFactors(factors[1:])
      else:
         divs = divisorsFromFactors(factors[1:])
         alldivs = []
         for power in range(0, factors[0][1]+1):
            alldivs += map(lambda x: x * base ** power, divs)
         alldivs.sort()
         return alldivs

n = int(sys.argv[1])
f = factorize(n)

f2a = map(lambda x: str(x[0]) if x[1] == 1 else "^".join(map(str, x)), f)
f2s = " * ".join(f2a)
print str(n) + " = " + f2s

f1a = map(lambda x: [x[0]] * x[1], f)
f1b = reduce(lambda x,y: x + y, f1a, [])
f1s = " * ".join(map(str, f1b))
print str(n) + " = " + f1s

print

d = divisorsFromFactors(f)

d1s = "N/A" if not d else ", ".join(map(str, d))
print "Divisors: " + d1s

d2a = reduce(lambda x,y: x + y, d, 0)
d2b = d2a - abs(n)
d2c = d2b - abs(n)
d2s = "zero" if d2a == 0 else "unit" if d2b == 0 else "prime" if d2b == 1 else "deficient" if d2c < 0 else "perfect" if d2c == 0 else "abundant"
print "sigma_0(n) = " + str(len(d))
print "sigma_1(n) = " + str(d2a)
print "sigma_1(n)-n = " + str(d2b)
print "sigma_1(n)-2n = " + str(d2c)
print str(abs(n)) + " is " + d2s + "."

print

d3a = map(lambda x: str(d[x]) + "*" + str(d[len(d)-x-1]), range(0, (1 + len(d)) // 2))
d3s = "0*0" if not d3a else "\t".join(d3a)
print "Pairs:"
print d3s
