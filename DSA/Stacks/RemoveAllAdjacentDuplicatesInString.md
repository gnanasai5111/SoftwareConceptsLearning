# Remove All Adjacent Duplicates In String (LeetCode 1047)

## Problem Statement

Given a string `s`, repeatedly remove adjacent duplicate characters until no adjacent duplicates remain.

Return the final string.

---

## Examples

### Example 1

```text
Input:
s = "abbaca"

Output:
"ca"
```

Explanation:

```text
abbaca

↓

aaca

↓

ca
```

---

### Example 2

```text
Input:
s = "azxxzy"

Output:
"ay"
```

Explanation:

```text
azxxzy

↓

azzy

↓

ay
```

---

# Approach 1 - Brute Force

## Intuition

Repeatedly scan the string.

Whenever two adjacent characters are the same:

* Remove them.
* Build a new string.
* Repeat until no duplicates are found.

### Algorithm

1. Traverse the string.
2. Remove every adjacent duplicate pair.
3. Create a new string.
4. Repeat until one complete pass finds no duplicates.

### Time Complexity

**O(n²)**

Reason:

* We may scan the string multiple times.
* During every scan, we build a new string.

### Space Complexity

**O(n)**

A new string is created during every iteration.

---

# Approach 2 - Stack (Optimal)

## Intuition

The most recently added character is the only one that can become adjacent to the current character after previous removals.

Therefore, use a **Stack**.

For every character:

* If it matches the top of the stack, remove the top.
* Otherwise, push it.

---

## Algorithm

1. Create an empty stack.
2. Traverse the string.
3. If the stack is not empty and the top equals the current character:

   * Pop the stack.
4. Otherwise:

   * Push the current character.
5. Join all remaining characters in the stack.

---

## Solution

```python
class Solution(object):
    def removeDuplicates(self, s):

        stack = []

        for ch in s:

            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)
```

---

## Dry Run

Input

```text
abbaca
```

| Character | Stack |
| --------- | ----- |
| a         | a     |
| b         | a b   |
| b         | a     |
| a         | empty |
| c         | c     |
| a         | c a   |

Result:

```text
ca
```

---

## Time Complexity

**O(n)**

Reason:

* Every character is pushed at most once.
* Every character is popped at most once.
* `join()` traverses the remaining stack once.

Overall:

```text
O(n)
```

---

## Space Complexity

**O(n)**

Worst case:

```text
abcdef
```

No duplicates exist, so every character is stored in the stack.

---

# Why Stack?

After removing duplicates, the current character only needs to be compared with the **most recent unmatched character**.

Example:

```text
abbaca

a b b

↓

a

Now the next 'a' becomes adjacent to the previous 'a'.
```

The stack naturally keeps track of the most recent unmatched character, making it the perfect data structure for this problem.

---

# Interview Takeaways

* Brute Force repeatedly scans and rebuilds the string → **O(n²)**.
* Stack processes each character only once → **O(n)**.
* Every character is pushed and popped **at most once**.
* Use `stack[-1]` to access the top element.
* Use `"".join(stack)` to efficiently convert the stack into the final string without modifying it.

---

# Pattern Recognition

Think **Stack** when you see:

* Adjacent removals.
* Most recently processed element.
* Undoing previous work.
* LIFO behavior.
