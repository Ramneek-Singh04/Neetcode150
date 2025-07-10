Given:

List of nums

Output:
True or False

Condition:
If we read through the list and find a duplicate, then we return True, if there is no duplicate, we return False

The way this solution works is we start off by iterating through the list, for each number that we find, we add it to our dictionary and assign it a arbitrary value (in my case it is 1), since we only care about the key being in the dictionary. Then, we check against this dictionary the next time we iterate through the list. If the value we read matches a key in the dictionary, we know its a duplicate, and we can then return True, if we manage to go through the entire list and the if statement doesn't trigger, then we know there are no duplicates, and we can return False.
