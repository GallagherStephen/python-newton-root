#! /usr/bin/env python 3

#  stephen gallagher 
#  Calculate the sqrt of a number.


def sqrt(x):
  """
  calculate the sqare root of a number x
  """

  # check that x is positive
  if x < 0:
    print("error:negative number value was supplied")
    return -1
  else:
    print("here we go..")

  # z is an initial guess for the root.
  z = x / 2.0

  # continuously improve the guess .
  while abs(x - (z*z)) > 0.0000001:
    z = z - (((z*z) - x) / ( 2 * z))

  return z
myVal = 63.0
print("the sqrt  of ", myVal , "is" ,sqrt (myVal))



