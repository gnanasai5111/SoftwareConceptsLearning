# Min Stack (LeetCode 155)

## Problem Statement

Design a stack that supports the following operations in **O(1)** time:

* `push(value)` → Push an element onto the stack.
* `pop()` → Remove the top element.
* `top()` → Return the top element.
* `getMin()` → Return the minimum element currently present in the stack.

---

## Example

```text
Operations:

push(5)
push(2)
push(8)
getMin()
pop()
getMin()
pop()
getMin()
```

Output

```text
2
2
5
```

Explanation

```text
After push(5)

Main Stack
5

Minimum = 5

--------------------

After push(2)

Main Stack
2
5

Minimum = 2

--------------------

After push(8)

Main Stack
8
2
5

Minimum = 2

--------------------

pop()

Main Stack
2
5

Minimum = 2

--------------------

pop()

Main Stack
5

Minimum = 5
```

---

# Approach 1 - Brute Force

## Intuition

Use a normal stack.

Whenever `getMin()` is called:

* Traverse the entire stack.
* Find the smallest element.
* Return it.

---

## Algorithm

1. Push normally.
2. Pop normally.
3. Return top normally.
4. For `getMin()`, traverse the stack and find the minimum.

---

## Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| push      | O(1)       |
| pop       | O(1)       |
| top       | O(1)       |
| getMin    | O(n) ❌     |

---

## Space Complexity

```text
O(n)
```

---

## Why is it not optimal?

Every call to `getMin()` requires scanning the entire stack.

The problem requires **all operations** to run in **O(1)** time.

---

# Approach 2 - Two Stacks (Optimal)

## Intuition

Maintain two stacks:

### 1. Main Stack

Stores all elements.

### 2. Min Stack

Stores the **minimum value after every push**.

**Important:**

The Min Stack does **not** store the pushed values.

It stores the answer to the question:

> **"What is the minimum element in the main stack after this push?"**

---

## Example

Operations

```text
push(5)
push(2)
push(8)
push(1)
```

Main Stack

```text
Top
1
8
2
5
```

Min Stack

```text
Top
1
2
2
5
```

Notice:

* When `8` is pushed, the minimum is still `2`.
* Therefore, we push **2** into the Min Stack instead of **8**.

---

## Why are duplicate minimum values stored?

Suppose

```text
push(5)
push(2)
push(7)
```

Main Stack

```text
Top
7
2
5
```

Min Stack

```text
Top
2
2
5
```

If `7` is popped,

Main Stack

```text
Top
2
5
```

Min Stack

```text
Top
2
5
```

The minimum is still **2**.

If we had not stored the second `2`, we would lose track of the current minimum and would need to traverse the stack again.

Storing duplicate minimum values allows `getMin()` to remain **O(1)**.

---

## Algorithm

### push(value)

* Push the value into the Main Stack.
* If the Min Stack is empty:

  * Push the value.
* Else:

  * If the new value is smaller than or equal to the current minimum:

    * Push the new value.
  * Otherwise:

    * Push the current minimum again.

---

### pop()

* Pop from the Main Stack.
* Pop from the Min Stack.

Both stacks always remain synchronized.

---

### top()

Return the top element of the Main Stack.

---

### getMin()

Return the top element of the Min Stack.

---

## Solution

```python
class MinStack(object):

    def __init__(self):
        self.mainStack = []
        self.minStack = []

    def push(self, value):

        self.mainStack.append(value)

        if not self.minStack:
            self.minStack.append(value)

        elif value <= self.minStack[-1]:
            self.minStack.append(value)

        else:
            self.minStack.append(self.minStack[-1])

    def pop(self):

        if self.mainStack:
            self.mainStack.pop()
            self.minStack.pop()

    def top(self):

        return self.mainStack[-1] if self.mainStack else -1

    def getMin(self):

        return self.minStack[-1] if self.minStack else -1
```

---

## Dry Run

Operations

```text
push(5)
push(2)
push(8)
push(1)
```

| Operation | Main Stack | Min Stack |
| --------- | ---------- | --------- |
| push(5)   | 5          | 5         |
| push(2)   | 5,2        | 5,2       |
| push(8)   | 5,2,8      | 5,2,2     |
| push(1)   | 5,2,8,1    | 5,2,2,1   |

Now

```text
getMin()
```

returns

```text
1
```

---

Pop

Main Stack

```text
5
2
8
```

Min Stack

```text
5
2
2
```

Now

```text
getMin()
```

returns

```text
2
```

No traversal is required.

---

# Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| push      | O(1)       |
| pop       | O(1)       |
| top       | O(1)       |
| getMin    | O(1)       |

---

# Space Complexity

Two stacks are maintained.

Each can store up to **n** elements.

```text
O(2n)
```

Ignoring constants,

```text
O(n)
```

---

# Pattern Recognition

Think **extra data structure** whenever a problem asks:

* Normal operations.
* Plus one additional operation.
* All in **O(1)**.

Instead of recomputing information repeatedly, maintain extra information while performing updates.

---

# Interview Takeaways

* A normal stack cannot return the minimum in **O(1)**.
* The Min Stack stores the **minimum after every push**, not just distinct minimum values.
* Duplicate minimum values are intentionally stored.
* Both stacks always have the same number of elements.
* Every push has a corresponding push in the Min Stack.
* Every pop has a corresponding pop in the Min Stack.
* `getMin()` simply returns the top of the Min Stack, making it **O(1)**.
