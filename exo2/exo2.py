"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""

"""
Create unit test using those cases:
fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)
"""
import unittest


class Solution:
  def __init__(self,first: str, second: str):
      self._first = first
      self._second = second

   
  def ends_with(self,) -> bool:
    print(f"Firsttype: {self._first}, Secondtype: {self._second}")
    return self._first.endswith(self._second)
  
A = Solution("Jesuis","s")
print(A.ends_with())



class TestSolution(unittest.TestCase):
    def test_fixed_tests_True(self):
        fixed_tests_True = (
            ("samurai", "ai"),
            ("ninja", "ja"),
            ("sensei", "i"),
            ("abc", "abc"),
            ("abcabc", "bc"),
            ("fails", "ails"),
        )

        for first, second in fixed_tests_True:
            sol = Solution(first, second)  # Créer une nouvelle instance avec les attributs
            with self.subTest(first=first, second=second):
                self.assertTrue(sol.ends_with(), f"Expected True but got False for {first}, {second}")

    def test_fixed_tests_False(self):
        fixed_tests_False = (
            ("sumo", "omo"),
            ("samurai", "ra"),
            ("abc", "abcd"),
            ("ails", "fails"),
            ("this", "fails"),
            ("spam", "eggs"),
        )

        for first, second in fixed_tests_False:
            sol = Solution(first, second)  # Créer une nouvelle instance avec les attributs
            with self.subTest(first=first, second=second):
                self.assertFalse(sol.ends_with(), f"Expected False but got True for {first}, {second}")

# Exécuter les tests
if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
