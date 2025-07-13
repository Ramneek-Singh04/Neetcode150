Problem Name:
🟢 Two Sum

Given:
A string of nums, nums
A target value we are trying to add up to, target

Output:
The indexes of the numbers that add to the target, there is only one possible solution

Condition:
There is a solution where two indicies of the string add up to the target value, return them in a list

Time Complexity:

O(n) -> Since we are going throught the list one time and adding all elements that we see into a dictionary to check against for fast O(1) lookup times. We can then just return these values

Space Complexity:
O(n) because in the worst case if the solution is at the very end of the list we are inserting elements one by one into a dictionary, and the max amount is the length of the list, which is n
