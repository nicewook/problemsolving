import unittest
"""
replace space with %20
ex)"hey how are you    "
return hey%20how%20are%20you
"""

def encode_space(str):
    return str.strip().replace(" ", "%20")

input1="hey how are you   "
input2="hey%20how%20are%20you"

class encode_space_test(unittest.TestCase):
    def test(self):
        self.assertEqual(input2, encode_space(input2))


print( "input1.strip(): --", input1.strip(), "--")
print("input1.strip().replace(' ','%20'): --", input1.strip().replace(" ", "%20"), "--")
