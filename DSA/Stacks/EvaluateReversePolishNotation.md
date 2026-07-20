# Evaluate Reverse Polish Notation

## Problem Statement

You are given an array of strings `tokens` representing an arithmetic expression in **Reverse Polish Notation (Postfix Expression)**.

Evaluate the expression and return its value.

Rules:

* Valid operators: `+`, `-`, `*`, `/`
* Division truncates toward zero.
* The input is always a valid RPN expression.

---

# What is Reverse Polish Notation (RPN)?

In Reverse Polish Notation, the **operator comes after its operands**.

Example:

```text
Infix:
(2 + 1) * 3

Postfix (RPN):
2 1 + 3 *
```

Evaluation:

```text
2 1 + 3 *

↓

2 + 1 = 3

↓

3 3 *

↓

3 × 3 = 9
```

---

# Approach 1: Brute Force

## Intuition

Repeatedly scan the array until you find:

```text
number number operator
```

Evaluate that operation and replace those three elements with the result.

Continue until only one value remains.

---

## Algorithm

1. Traverse the array.
2. Find two consecutive operands followed by an operator.
3. Evaluate the expression.
4. Replace the three elements with the result.
5. Repeat until only one element remains.

---

### Example

```text
Input:

["2","1","+","3","*"]
```

Pass 1

```text
2 1 + 3 *

↓

3 3 *
```

Pass 2

```text
3 3 *

↓

9
```

Answer:

```text
9
```

---

### Complexity

* **Time:** `O(n²)`
* **Space:** `O(n)`

---

# Approach 2: Stack (Optimal)

## Intuition

Whenever we encounter:

* A **number**, store it.
* An **operator**, remove the last two numbers, perform the operation, and push the result back.

Since the **most recently stored operands are always used first**, this follows the **Last In First Out (LIFO)** principle.

A **Stack** is the perfect data structure.

---

## Algorithm

1. Create an empty stack.
2. Traverse each token.
3. If it is a number, push it onto the stack.
4. If it is an operator:

   * Pop the top two operands.
   * Perform the operation.
   * Push the result back.
5. The final element in the stack is the answer.

---

### Code

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))

        return stack.pop()
```

---

### Dry Run

Input

```text
["2","1","+","3","*"]
```

| Token | Stack |
| ----- | ----- |
| 2     | 2     |
| 1     | 2,1   |
| +     | 3     |
| 3     | 3,3   |
| *     | 9     |

Answer

```text
9
```

---

### Why subtraction and division use `a op b`?

Suppose the stack contains:

```text
Top

4
10
```

The top element (`4`) is popped first.

```python
b = stack.pop()   # 4
a = stack.pop()   # 10
```

Subtraction:

```text
10 - 4
```

Division:

```text
10 / 4
```

If we reverse the operands, the answer becomes incorrect.

---

### Complexity

* **Time:** `O(n)`
* **Space:** `O(n)`

---

# Pattern Recognition

Whenever you encounter:

* Postfix Expression (Reverse Polish Notation)
* Prefix Expression
* Expression Evaluation
* Arithmetic Parsing
* Calculators
* Operand-Operator processing

Think:

> **Stack**

---

# Comparison

| Approach    | Time    | Space  | Notes                                                 |
| ----------- | ------- | ------ | ----------------------------------------------------- |
| Brute Force | `O(n²)` | `O(n)` | Repeatedly scans and reduces the expression.          |
| Stack       | `O(n)`  | `O(n)` | Processes every token exactly once. Optimal solution. |

---

# Key Takeaways

* Reverse Polish Notation is naturally evaluated from left to right.
* The last two operands are always used when an operator appears.
* This follows the **LIFO (Last In, First Out)** principle.
* A Stack allows each token to be processed exactly once, making it the optimal solution.
* Always remember the operand order:

  * `a = second pop`
  * `b = first pop`
  * Perform `a operator b`, especially for subtraction and division.
