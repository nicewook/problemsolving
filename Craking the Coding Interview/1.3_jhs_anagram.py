import unittest

def anagram(str1, str2):
    if ''.join(sorted(str1.lower())).strip() == ''.join(sorted(str2.lower())).strip():
        return True
    else:
        return False

class anagramTest(unittest.TestCase):
    def test(self):
        self.assertTrue(anagram("liS ten", "silen T"))
        self.assertFalse(anagram("abc", "adc"))

string1 = "liS te  n"

print ("string1 =", string1)

result = string1.lower()
print ("result = string1.lower(): ", result)

result = sorted(result)
print ("result = sorted(result): ", result)

result = sorted(result)
print ("result = sorted(result): ", result)

result = ''.join(result)
print ("result = ''.join(result): ", result)

result = result.strip()
print ("result = result.strip(): ", result)
