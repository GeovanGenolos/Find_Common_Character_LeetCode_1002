# This is my code inn solving LeetCode problem 1002: Find Common Characters

```
from typing import List
from collections import Counter

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        """
        Find common characters among all strings in the given list.

        Parameters:
        A (List[str]): A list of strings.

        Returns:
        List[str]: A list of common characters that appear in each string.
        """
        # Initialize the common counter with the character counts from the first word
        common_count = Counter(A[0])
        
        # Update the common counter with the intersection of all other word counters
        for word in A[1:]:
            word_count = Counter(word)
            common_count &= word_count  # Intersection: min(counts)

        # Convert the counter to a list of characters
        result = list(common_count.elements())
        
        return result

solution = Solution()  # Instantiate the Solution class

# First example
words1 = ["bella", "label", "roller"]
print(solution.commonChars(words1))  # Output: ['e', 'l', 'l']

# Second second
words2 = ["cool", "lock", "cook"]
print(solution.commonChars(words2))  # Output: ['c', 'o']
```

# Explanation of Example 1:

1. Instance Method:

- 'commonChars' is an instance method, meaning it should be called on an instance of the 'Solution' class.
- 'solution = Solution()' creates an instance of the 'Solution' class.

2. Calling the Method:

- 'solution.commonChars(words)' correctly calls the method on the instance solution.

This ensures that the method receives the necessary 'self' argument automatically, as well as the 'A' argument that you pass explicitly.

#Explanation of Example 2:
For the input '["cool", "lock", "cook"]':

- Initial 'common_count' from "cool": '{'c': 1, 'o': 2, 'l': 1}'
- After intersection with "lock": '{'c': 1, 'o': 1, 'l': 1}'
- After intersection with "cook": '{'c': 1, 'o': 1}'
- The final result is '['c', 'o''].
