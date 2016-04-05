import unittest

import baseconverter

class Test2(unittest.TestCase):
  tests = []
  results = []

  def test(self):
    for conv, result in zip(self.tests, self.results):
      self.assertEqual(conv.convert(), result)


  def setUp(self):       
    converter = baseconverter.DecimalBaseConverter("1001",2)
    self.tests.append(converter)
    self.results.append(9)
         
