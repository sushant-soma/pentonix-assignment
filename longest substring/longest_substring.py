'''
1. checks for a special case wehere the lenght of the input string would be 1 and it would return 1 as it is the length of the longest substring that is itself
2. uses a set 'solutionSet' to store unique, non-repeating characters. This set will be used to keep track of the characters in the current substring
3. two pointers 'l' and 'r' are used to keep track of the current substring and are updated as required
4. variable 'res' holds the length of the longest substring and is returned in the end
5. a loop runs from starting of the given string to the end, until 'r' reaches the end element 
6. checks every index of the string, if it is present in the substring, then the leftmost element of the substring is removed and the left pointer is increased until the next element is not unique
7. 'r - l + 1' represents the length of the substring
8. finally returns res
'''

def longest_substring(s):

    if len(s) == 1:         # if length of input string is 1 then length of longest substring is 1
        return 1
    
    solutionSet = set()     # a set to store unique non repeating elements 

    l = 0                   # left pointer
    res = 0                 # holds the length of longest substring

    for r in range(len(s)):             # r moves until the last element of the given string
        while s[r] in solutionSet:      # until the current element s[r] is already present in the set
            solutionSet.remove(s[l])    # if the current element is present, remove the leftmost element of the substring and increment the left pointer
            l += 1                      
        
        solutionSet.add(s[r])           # keeps adding elements in every for loop iteration to get all the characters in the string
        res = max(res, r - l + 1)       # keeps track of the length of the longest substring

    return res 

s = input("Enter the String: ")
print("\nLength of Longest Substring without Repeating Characters:",longest_substring(s))