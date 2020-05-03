from bot import AIchat
import unittest

class TestCode(unittest.TestCase):
  def testsimple(self):
    self.assertEqual(AIchat.unsettledFees(self,'Miranda','Erin','C','0'),"Unsettled charges for Miranda, Erin C. amounts to: 0")

if __name__=='__main__':
  unittest.main(exit=False)