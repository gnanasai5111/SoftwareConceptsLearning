# Remove All Adjacent Duplicates In String 

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

* Traverse the string from left to right.
* Whenever two adjacent characters are equal, remove both of them.
* Build a **new string** without those duplicate pairs.
* Repeat this process until one complete traversal finds no adjacent duplicates.

This approach repeatedly scans and rebuilds the string.

---

## Algorithm

1. Traverse the string.
2. If two adjacent characters are equal, skip both.
3. Otherwise, add the current character to a new string.
4. After one complete pass:

   * If no duplicates were removed, return the new string.
   * Otherwise, repeat the process using the newly built string.

---

## Brute Force Solution

```python
class Solution(object):
    def removeDuplicates(self, s):
        length = len(s)

        while True:

            foundDuplicates = False
            i = 0
            newString = ""

            while i < length:

                if i < length - 1 and s[i] == s[i + 1]:
                    foundDuplicates = True
                    i += 2
                else:
                    newString += s[i]
                    i += 1

            if not foundDuplicates:
                return newString

            s = newString
            length = len(s)
```

---

## Dry Run

Input

```text
abbaca
```

### Pass 1

```text
a b b a c a

↓

a a c a
```

New String

```text
aaca
```

---

### Pass 2

```text
a a c a

↓

c a
```

New String

```text
ca
```

---

### Pass 3

```text
c a
```

No adjacent duplicates remain.

Return

```text
ca
```

---

## Time Complexity

### O(n²)

Reason:

* Each pass scans the entire string → **O(n)**.
* In the worst case, we may perform multiple scans.

Example:

```text
abccba

↓

abba

↓

aa

↓

""
```

Therefore,

```text
O(n) × O(n) = O(n²)
```

---

## Space Complexity

### O(n)

A new string is created during every pass.

---

# Approach 2 - Stack (Optimal)

## Intuition

The current character only needs to be compared with the **most recent unmatched character**.

A **Stack** naturally stores the most recently processed character.

For every character:

* If it matches the top of the stack, remove the top.
* Otherwise, push it.

Since each character is pushed and popped at most once, we avoid repeated scans.

---

## Algorithm

1. Create an empty stack.
2. Traverse the string.
3. If the stack is not empty and the top equals the current character:

   * Pop the stack.
4. Otherwise:

   * Push the current character.
5. Join the remaining stack into a string.

---

## Optimal Solution

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

Result

```text
ca
```

---

## Time Complexity

### O(n)

Reason:

Each character is:

* Pushed at most once.
* Popped at most once.

Joining the stack also takes **O(n)**.

Overall:

```text
O(n)
```

---

## Space Complexity

### O(n)

Worst case:

```text
abcdef
```

No duplicates exist, so every character is stored in the stack.

---

# Why Stack?

Example:

```text
abbaca
```

Initially:

```text
a b b
```

After removing:

```text
bb
```

The string becomes:

```text
aaca
```

Now the two `'a'` characters become adjacent.

The only character we need to compare the current character with is the **most recently unmatched character**.

A stack maintains exactly this information.

---

# Brute Force vs Optimal

| Feature                      | Brute Force | Stack |
| ---------------------------- | ----------- | ----- |
| Repeated scans               | ✅ Yes       | ❌ No  |
| Builds new string repeatedly | ✅ Yes       | ❌ No  |
| Time Complexity              | O(n²)       | O(n)  |
| Space Complexity             | O(n)        | O(n)  |

---

# Pattern Recognition

Think **Stack** whenever you see:

* Adjacent removals.
* Most recently processed element.
* Undoing previous work.
* LIFO behavior.

---

# Interview Takeaways

* Start with the brute-force approach by repeatedly removing adjacent duplicates.
* Identify the repeated work:

  * Multiple scans.
  * Rebuilding the string.
* Optimize using a stack.
* Every character is pushed and popped at most once.
* Use `stack[-1]` to access the top element.
* Use `"".join(stack)` to efficiently convert the stack into the final answer without modifying the stack.
