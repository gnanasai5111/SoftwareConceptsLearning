# Stack

## What is a Stack?

A **Stack** is a **linear data structure** that stores elements sequentially and follows the **LIFO (Last In, First Out)** principle.

Example:

```
Push: 10, 20, 30

Top
30
20
10

Pop -> 30
```

The last element inserted is the first element removed.

---

## Stack is an ADT (Abstract Data Type)

A **Stack** is an **Abstract Data Type (ADT)** because it defines **what operations are supported**, but **does not specify how they are implemented**.

It only defines the behavior:

* `push()`
* `pop()`
* `peek()`
* `empty()`
* `size()`

The implementation can use different underlying data structures such as:

* Arrays
* Linked Lists

---

# Stack Operations

### 1. Push

Adds an element to the top of the stack.

### 2. Pop

Removes and returns the top element.

### 3. Peek (Top)

Returns the top element without removing it.

### 4. Empty

Returns `True` if the stack is empty; otherwise returns `False`.

### 5. Size

Returns the number of elements in the stack.

---

# Implementation

## 1. Using Arrays

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.items:
            return self.items.pop()
        return -1

    def peek(self):
        if self.items:
            return self.items[-1]
        return -1

    def empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
```

### Time Complexity

| Operation | Complexity     |
| --------- | -------------- |
| Push      | O(1) amortized |
| Pop       | O(1)           |
| Peek      | O(1)           |
| Empty     | O(1)           |
| Size      | O(1)           |

### Why is `push()` O(1) amortized?

Most `push()` operations simply append an element to the end of the array and take **O(1)** time.

Occasionally, when the array becomes full, Python allocates a larger array and copies all existing elements into it before inserting the new element. That particular operation takes **O(n)**.

Since resizing happens only occasionally, the **average cost over many push operations remains O(1)**. This is called **amortized O(1)**.

---

## 2. Using Linked List

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.index = 0

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.index += 1

    def pop(self):
        if self.top:
            removed = self.top
            self.top = self.top.next
            self.index -= 1
            return removed.value
        return -1

    def peek(self):
        return self.top.value if self.top else -1

    def empty(self):
        return self.size() == 0

    def size(self):
        return self.index
```

### Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| Push      | O(1)       |
| Pop       | O(1)       |
| Peek      | O(1)       |
| Empty     | O(1)       |
| Size      | O(1)       |

### Why do we use the head as the top?

In a singly linked list:

```
Top
 ↓
30 → 20 → 10
```

* **Push** inserts a new node at the head.
* **Pop** removes the head node.

Both operations take **O(1)** time.

If the top were at the tail, `pop()` would require traversing the entire list, resulting in **O(n)** time.

---

# Arrays vs Linked Lists

| Feature           | Array          | Linked List                                |
| ----------------- | -------------- | ------------------------------------------ |
| Push              | O(1) amortized | O(1)                                       |
| Pop               | O(1)           | O(1)                                       |
| Extra Memory      | No             | Yes (stores `next` pointer for every node) |
| Cache Locality    | Excellent      | Poor                                       |
| Resizing Required | Yes            | No                                         |

---

# Cache Locality

Modern CPUs have a small, very fast memory called the **cache**.

Arrays store elements in **contiguous (adjacent) memory locations**:

```
10 20 30 40 50
```

When the CPU loads one element, nearby elements are often loaded into the cache as well. This is called **good cache locality**, making array access very fast.

Linked list nodes are stored at **different memory locations**:

```
10 --> 20 --> 30 --> 40
```

Each node can be located anywhere in memory, so the CPU often has to fetch each node separately from RAM. This results in **poor cache locality**.

Although both array-based and linked-list-based stacks have **O(1)** operations, **array-based stacks are often faster in practice** because:

* Better cache locality.
* Less memory overhead (no extra pointer per node).
* Fewer memory allocations.

---

# Interview Takeaways

* Stack is a **Linear Data Structure**.
* Stack follows **LIFO (Last In, First Out)**.
* Stack is an **ADT**, not a specific implementation.
* It can be implemented using **Arrays** or **Linked Lists**.
* Array `push()` is **O(1) amortized** due to occasional resizing.
* Linked list `push()` and `pop()` are always **O(1)**.
* In a linked-list implementation, **the head acts as the top of the stack**.
* Arrays are usually faster in practice because of **better cache locality**.
