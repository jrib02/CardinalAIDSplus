from bot import AIchat
import unittest

class TestCode(unittest.TestCase):
  def testsimple(self):
    fallbackOptions = ["You have either entered an invalid batch number or didn't specify one. Could you specify a valid batch number? ", 
      "I don't think you've entered a valid batch number. Can you re-enter that?", 
      "Please enter a valid batch number."]

    testMessage = "What is the schedule of enrollment"
    self.assertIn(AIchat.schedEnroll(self,testMessage),fallbackOptions)

if __name__=='__main__':
  unittest.main(exit=False)