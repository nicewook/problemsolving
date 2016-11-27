"""
return true if the string doesn't have duplicate characters
return false if the string has duplicate character 
"""
import unittest

def isUniqChars(str):
    # assume characters are ASCII, total 256 characters
    # if the string is greater than 256, there is duplicate
    if len(str) > 256:
        return False
    # initialize boolean array with [False]. ASCII characters range 0-255
    hash = [False] * 256

    for ch in str:
        # if boolean array is true, then there is duplicate
        # ord(ch) returns ASCII code(=number) of character
        if hash[ord(ch)] is True:
            return False
        # if the value in hash is False, the value is not duplicate yet
        else:
            hash[ord(ch)] = True
    return True


class isUniqCharsTest(unittest.TestCase):
    def test(self):
        input_unique = "abcde"
        input_not_unique = "abcdea"
        self.assertTrue(isUniqChars(input_unique))
        self.assertFalse(isUniqChars(input_not_unique))

#jhs test
result=isUniqChars("adbdsetsdf")
if result == True:
    print "ttttt"
else:
    print "ffffff"

if __name__ == "__main__":
    unittest.main()
