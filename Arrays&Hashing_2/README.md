Problem Name:
🟢 Is Anagram

Given:

A string s
A string t

Output:
True or False

Condition:
If these two strings are anagrams (meaning they have the same amount of letters just different order) then return True, otherwise False

The way this solution works is that we iterate through in each string and keep track using a dictionary. Before doing this we can check if these two strings are the same length, becuase if they are not, then they break the definition of a anagram and therefore are not anagrams. Lookup and write times are O(1) so storing in a Dictionary is efficient. We then compare these two dictionaries and ensure that they are the same, if they are, then return True.

Time Complexity:

O(n) -> We are reading through two strings, assuming the worst case where they are anagrams, is only O(2n) which is O(n) simplified. Reading, comparing dictionaries is O(1) time so we are good.
\*if we sort the strings using built in its actually slower, its nlogn time, which is slower than what we have.

Space Complexity:
O(k) where k is the number of unique elements in each array. If its just the alphabet, its O(1) since its O(26) which is just O(1) simplified.
\*if we did the sorted solution it would be O(n) space because sorting takes extra space.
