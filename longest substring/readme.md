# Longest Substring without Repeating Characters

This Python script finds and returns the length of the longest substring in a given input string without repeating characters.

## Algorithm Overview

The script uses a sliding window approach with two pointers (`l` and `r`) to traverse the input string. Here's a brief overview of the algorithm:

1. It checks for a special case where the length of the input string is 1, and in this case, it returns 1 as the length of the longest substring because the string itself is unique.

2. The algorithm uses a set called `solutionSet` to store unique, non-repeating characters. This set is used to keep track of the characters in the current substring.

3. Two pointers, `l` (left) and `r` (right), are employed to define the current substring. These pointers are updated as needed.

4. The variable `res` holds the length of the longest substring and is returned at the end.

5. A loop runs from the beginning of the given string to the end, until `r` reaches the last element of the string.

6. At each iteration, the algorithm checks if the character at the current index `r` is already present in the `solutionSet`. If it is, the algorithm removes the leftmost element of the substring (pointed to by `l`) and increments `l` until the next element is not a duplicate.

7. The length of the current substring is calculated as `r - l + 1`.

8. The algorithm keeps track of the maximum length found in the `res` variable.

9. Finally, it returns the value of `res`, which represents the length of the longest substring without repeating characters.

## How to Use

1. Ensure you have Python installed on your system.

2. Clone this repository
    ```bash
    git clone https://github.com/sushant-soma/pentonix-assignment.git

3. navigate to the dictory that contains longest substring
    ```bash
    cd longest substring

4. Run the script by providing an input string when prompted:

   ```bash
   python longest_substring.py
