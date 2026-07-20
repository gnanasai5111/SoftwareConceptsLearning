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
operand operand operator
```

Evaluate the operation, replace these three elements with the computed result, and start scanning again. Continue until only one element remains.

---

## Algorithm

1. Traverse the array from left to right.
2. Find the first operator.
3. The previous two elements are its operands.
4. Evaluate the expression.
5. Replace:

   * Operand 1
   * Operand 2
   * Operator
     with the calculated result.
6. Repeat until only one element remains.

---

## Code

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        while len(tokens) > 1:
            i = 0

            while i < len(tokens):

                if tokens[i] in "+-*/":

                    a = int(tokens[i - 2])
                    b = int(tokens[i - 1])
                    op = tokens[i]

                    if op == "+":
                        ans = a + b
                    elif op == "-":
                        ans = a - b
                    elif op == "*":
                        ans = a * b
                    else:
                        ans = int(a / b)

                    tokens = tokens[:i - 2] + [str(ans)] + tokens[i + 1:]
                    break

                i += 1

        return int(tokens[0])
```

---

## Dry Run

Input

```text
["2","1","+","3","*"]
```

### Iteration 1

Operator found:

```text
2 1 +
```

Evaluate:

```text
2 + 1 = 3
```

Replace:

```text
["2","1","+","3","*"]

↓

["3","3","*"]
```

---

### Iteration 2

Operator found:

```text
3 3 *
```

Evaluate:

```text
3 * 3 = 9
```

Replace:

```text
["3","3","*"]

↓

["9"]
```

Answer

```text
9
```

---

## Complexity

* **Time:** `O(n²)`
* **Space:** `O(n)`

### Why O(n²)?

* Every iteration scans the list to find the next operator.
* Replacing three elements with one creates a new list.
* This process repeats until only one value remains.

---

# Approach 2: Stack (Optimal)

## Intuition

Whenever we encounter:

* A **number**, push it onto the stack.
* An **operator**, pop the last two numbers, evaluate the expression, and push the result back.

Since the **most recently stored operands are always used first**, this follows the **Last In, First Out (LIFO)** principle.

A **Stack** is the ideal data structure.

---

## Algorithm

1. Create an empty stack.
2. Traverse each token.
3. If it is a number, push it onto the stack.
4. If it is an operator:

   * Pop the top two operands.
   * Perform the operation.
   * Push the result back.
5. The remaining element in the stack is the answer.

---

## Code

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

## Dry Run

Input

```text
["2","1","+","3","*"]
```

| Token | Stack |
| ----- | ----- |
| 2     | 2     |
| 1     | 2, 1  |
| +     | 3     |
| 3     | 3, 3  |
| *     | 9     |

Answer

```text
9
```

---

## Why do subtraction and division use `a op b`?

Suppose the stack contains:

```text
Top

4
10
```

The top element is popped first.

```python
b = stack.pop()   # 4
a = stack.pop()   # 10
```

Therefore,

```text
10 - 4
10 / 4
```

not

```text
4 - 10
4 / 10
```

The operand order is important for subtraction and division.

---

## Complexity

* **Time:** `O(n)`
* **Space:** `O(n)`

---

# Pattern Recognition

Whenever you encounter:

* Reverse Polish Notation (Postfix Expression)
* Prefix/Postfix Evaluation
* Expression Evaluation
* Arithmetic Parsing
* Calculators
* Operand-Operator Processing

Think:

> **Stack (LIFO)**

---

# Comparison

| Approach    | Time    | Space  | Notes                                                                                         |
| ----------- | ------- | ------ | --------------------------------------------------------------------------------------------- |
| Brute Force | `O(n²)` | `O(n)` | Repeatedly scans the list, evaluates one operation, replaces it with the result, and repeats. |
| Stack       | `O(n)`  | `O(n)` | Processes every token exactly once. Optimal solution.                                         |

---

# Key Takeaways

* Reverse Polish Notation places operators **after** their operands.
* In the brute-force approach, repeatedly replace **operand operand operator** with the computed result until only one value remains.
* In the optimal solution, use a **Stack** because operators always use the two most recently seen operands.
* For subtraction and division, always perform:

  * `a = second pop`
  * `b = first pop`
  * Compute `a operator b`.
* The Stack solution is the standard interview approach because it evaluates the expression in a single pass.
