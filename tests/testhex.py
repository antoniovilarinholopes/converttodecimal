import unittest

import baseconverter

class TestHex(unittest.TestCase):
  tests = []
  results = []

  def test(self):
    for conv, result in zip(self.tests, self.results):
      self.assertEqual(conv.convert(), result)


  def setUp(self):       
    converter = baseconverter.DecimalBaseConverter("F",16)
    self.tests.append(converter)
    self.results.append(15)
    converter = baseconverter.DecimalBaseConverter("1E",16)
    self.tests.append(converter)
    self.results.append(30)
    converter = baseconverter.DecimalBaseConverter("21",16)
    self.tests.append(converter)
    self.results.append(33)
         
