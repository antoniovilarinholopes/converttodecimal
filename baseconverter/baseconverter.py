#!/usr/bin/python3.4

class DecimalBaseConverter:
  def __init__(self, number, base):
    self._number = number
    self._base = base
    self._zero_ascci = 48
    self._a_ascci = 55

  def convert(self):

    if(not all(c.isalnum() for c in list(self._number))):
      print("Invalid digit in number provided")
      exit(1)
    
    digits = map(lambda c : ord(c) - self._zero_ascci if(c.isdigit()) else ord(c.upper()) - self._a_ascci, self._number)

    invalid_digits = filter(lambda d : d > self._base, digits)
    if(invalid_digits):
      invalid_digits = map(lambda c : chr(c + self._zero_ascci) if(c < 10) else chr(c + self._a_ascci).upper(), invalid_digits)
      print("Using invalid digits {} for base {}".format(invalid_digits, self._base))
      exit(1)

    num_digits = len(self._number)
    max_power = num_digits - 1
    powers = range(max_power, -1, -1)
    #decimal_value = sum([digit * (base ** power) for digit, power in zip(digits,powers)] )
    return sum([digit * (self._base ** power) for digit, power in zip(digits,powers)] )


if __name__ == "__main__":
  import sys

  def dump():
    print("Usage: number base")

  assert(len(sys.argv) == 3) , dump()

  num = sys.argv[1]
  base = int(sys.argv[2])

  converter = DecimalBaseConverter(num, base)
  print ("Converted {} in base {} to {}".format(num, base, converter.convert()))
