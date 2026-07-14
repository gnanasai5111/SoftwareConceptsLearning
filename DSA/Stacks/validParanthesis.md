# Valid Parentheses

## Problem Statement

Given a string `s` containing only the characters:

* `(`
* `)`
* `{`
* `}`
* `[`
* `]`

Determine whether the input string is **valid**.

A string is considered valid if:

1. Every opening bracket has a corresponding closing bracket.
2. Brackets are closed in the correct order.
3. Every closing bracket matches the most recent unmatched opening bracket.

---

## Examples

### Example 1

```text
Input:
s = "()"

Output:
True
```

---

### Example 2

```text
Input:
s = "()[]{}"

Output:
True
```

---

### Example 3

```text
Input:
s = "(]"

Output:
False
```

Reason:

```
( should be closed by )
```

but it is closed by `]`.

---

### Example 4

```text
Input:
s = "([)]"

Output:
False
```

Reason:

```
(
[
)
]
```

The `)` tries to close `[`, which is incorrect.

---

### Example 5

```text
Input:
s = "{[]}"

Output:
True
```

Closing order:

```
{
[
]
}
```

The most recently opened bracket is always closed first.

---

# Intuition

Whenever we encounter an **opening bracket**, we don't yet know when it will be closed.

So, we store it for later.

When we encounter a **closing bracket**, it **must** match the **most recently opened bracket**.

This is exactly the **LIFO (Last In, First Out)** behavior of a **Stack**.

---

# Algorithm

1. Create an empty stack.
2. Create a dictionary that maps each closing bracket to its corresponding opening bracket.
3. Traverse the string.
4. If the current character is an opening bracket:

   * Push it onto the stack.
5. Otherwise (closing bracket):

   * If the stack is empty, return `False`.
   * Pop the top element.
   * If it does not match the expected opening bracket, return `False`.
6. After processing all characters:

   * If the stack is empty, return `True`.
   * Otherwise, return `False`.

---

# Solution

```python
class Solution(object):
    def isValid(self, s):
        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:

            if ch in "([{":
                stack.append(ch)

            elif not stack:
                return False

            elif stack.pop() != pairs[ch]:
                return False

        return not stack
```

---

# Time Complexity

### O(n)

Where **n** is the length of the string.

Reason:

* We traverse the string exactly once.
* Every character is processed only once.
* Each stack operation (`push`, `pop`, `peek`) takes **O(1)** time.

Therefore,

```
n × O(1) = O(n)
```

---

# Space Complexity

### O(n)

In the worst case, every character is an opening bracket.

Example:

```text
(((((((
```

All characters are pushed onto the stack.

Therefore, the stack may store **n** elements.

Space Complexity:

```
O(n)
```

---

# Pattern Recognition

This problem belongs to the **Stack** pattern because it involves:

* Matching pairs.
* Nested structures.
* Most recently opened element.
* LIFO behavior.
