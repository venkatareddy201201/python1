'''import unittest
def isValid(s):
    pattern=re.compile("(0/91)?[7-9][0-9]{9}")
    return pattern.match(s)
s="09959038535"
if(isValid(s)):
    print "valid"
else:
    print "inValid"

    '''

'''s='the is venkat hello chari hello'
x=re.findall(r'[\w\w]+ello',s)
print x'''

import unittest
class B(unittest.TestCase):
    def satish(self):
        print "this is satish here"
    def venkat():
        print "this is venkat here"
if __name__ == '__main__': 
    unittest.main()
