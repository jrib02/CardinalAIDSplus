from bot import AIchat
import unittest

class TestCode(unittest.TestCase):
  def testsimple(self):
    fallbackOptions = ["Can you be more specific for me?",
                     "I don't quite get what you're asking about scholarships.",
                     "Can you be more specific on scholarships?"]
    testMessage = "What is the contact of EECE?"
    self.assertIn(AIchat.scholarship(self,testMessage),fallbackOptions)

if __name__=='__main__':
  unittest.main(exit=False)