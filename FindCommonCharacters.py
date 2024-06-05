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
