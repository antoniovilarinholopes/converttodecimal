import unittest

import baseconverter

class TestOctal(unittest.TestCase):
  tests = []
  results = []

  def test(self):
    for conv, result in zip(self.tests, self.results):
      self.assertEqual(conv.convert(), result)


  def setUp(self):       
    converter = baseconverter.DecimalBaseConverter("7",8)
    self.tests.append(converter)
    self.results.append(7)
    converter = baseconverter.DecimalBaseConverter("8",8)
    self.tests.append(converter)
    self.results.append(8)
    converter = baseconverter.DecimalBaseConverter("10",8)
    self.tests.append(converter)
    self.results.append(8)
         
