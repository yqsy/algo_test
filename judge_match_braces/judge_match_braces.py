import unittest


class TestJudgeMatchBraces(unittest.TestCase):
    def test_1(self):
        self.assertTrue(judge_match_braces('[[]]'))

    def test_2(self):
        self.assertFalse(judge_match_braces('[[]'))

    def test_3(self):
        self.assertTrue(judge_match_braces(''))

    def test_4(self):
        self.assertFalse(judge_match_braces(']'))

def judge_match_braces(str):
    stack = []

    for c in str:
        if(c == '['):
            stack.append(c)
        if(c == ']'):
            try:
                stack.pop()
            except(IndexError):
                return False

    return True if len(stack) == 0 else False

if __name__ == '__main__':
    unittest.main()