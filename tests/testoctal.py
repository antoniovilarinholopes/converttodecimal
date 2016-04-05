import unittest

import baseconverter

class TestOctal(unittest.TestCase):
  tests = []
  results = []
  base = 8
  def test(self):
    for conv, result in zip(self.tests, self.results):
      self.assertEqual(conv.convert(), result)


  def setUp(self):       
    converter = baseconverter.DecimalBaseConverter("7",self.base)
    self.tests.append(converter)
    self.results.append(7)
    converter = baseconverter.DecimalBaseConverter("10",self.base)
    self.tests.append(converter)
    self.results.append(8)
         
