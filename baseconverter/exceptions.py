#!/usr/bin/python3.4

class InvalidDigitForBaseException(RuntimeError):
   def __init__(self, arg):
      self.args = arg

class NotAllNumCharsException(RuntimeError):
   def __init__(self, arg):
      self.args = arg
