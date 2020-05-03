from bot import AIchat
import unittest

class TestCode(unittest.TestCase):
  def testsimple(self):
    askResponses = ["What can I do for you?",
                        "What kind of assistance can I give?",
                        "What brought you to me?"]
    self.assertIn(AIchat.randomAsk(self),askResponses)

if __name__=='__main__':
  unittest.main(exit=False)