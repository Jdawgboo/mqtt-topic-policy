import unittest
from tool import validate
class TopicTests(unittest.TestCase):
 def test_policy(self):
  policy={'prefix':'site','max_depth':3,'allow_wildcards':False};self.assertEqual(validate('site/a/b',policy),[]);self.assertEqual(validate('other/a',policy),['wrong prefix']);self.assertIn('wildcard forbidden',validate('site/#',policy))
if __name__=='__main__':unittest.main()
