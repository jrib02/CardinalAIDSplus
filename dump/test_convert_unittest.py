from bot import AIchat
import unittest

class TestCode(unittest.TestCase):
  def testsimple(self):
    self.assertEqual(AIchat.convert(self,"Hi there!"),['Hi', 'there'])

if __name__=='__main__':
  unittest.main(exit=False)
