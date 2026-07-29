# 🎵 Spotify Premium Purchase - A Real World Journey

> A user wants to purchase Spotify Premium.

We'll build this feature together and discover three Design Patterns along the way.

```
User buys Premium
        │
        ▼
Factory Pattern
(Create the correct payment object)
        │
        ▼
Strategy Pattern
(Process the payment)
        │
        ▼
Observer Pattern
(Notify everyone that payment succeeded)
```

---

# 1. Strategy Pattern

## Why is it called Strategy?

Imagine you're travelling from Bangalore to Hyderabad.

You have multiple ways to reach the destination.

* Flight ✈️
* Train 🚆
* Bus 🚌
* Car 🚗

Your destination never changes.

Only **how** you reach it changes.

Each way is a different **strategy**.

Spotify works exactly the same way.

The goal is always

> Process Payment

But the way we process it changes.

* Credit Card
* UPI
* PayPal
* Apple Pay

The goal remains the same.

Only the algorithm changes.

That's why it's called the **Strategy Pattern**.

---

## Category

**Behavioral Design Pattern**

Behavioral patterns focus on **how an object performs a task or how objects interact.**

Here, the behavior is

> **How payment is processed.**

---

## Problem

Initially Spotify supports only **Credit Card** payments.

Everything works perfectly.

Then business comes with a new requirement.

> "Our Indian users prefer UPI."

You add UPI.

A month later.

> "Can we support PayPal?"

Done.

Next month.

* Apple Pay

Next month.

* Google Pay

Now ask yourself.

> **Should we keep modifying the same PaymentService every time a new payment method is added?**

Most beginners write something like this.

```python
class PaymentService:

    def process_payment(self, payment_type, amount):

        if payment_type == "credit":
            print("Credit Card")

        elif payment_type == "upi":
            print("UPI")

        elif payment_type == "paypal":
            print("PayPal")

        elif payment_type == "apple":
            print("Apple Pay")
```

Looks fine today.

But every new payment method forces you to modify the same class.

Tomorrow?

Samsung Pay.

Modify again.

Amazon Pay.

Modify again.

Crypto.

Modify again.

This violates the **Open/Closed Principle**.

---

## Solution

Instead of putting every payment algorithm inside one class...

Move every algorithm into its own class.

---

## Core Idea

> Encapsulate each algorithm into its own class and make them interchangeable.

---

## Step 1 - Create a Contract

```python
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

### What is a Contract?

Think of a contract like a job agreement.

Spotify says,

> "If you want to become a payment method, you MUST implement `pay()`."

Whether it's UPI or Credit Card doesn't matter.

Everyone follows the same contract.

---

## Step 2 - Concrete Strategies

```python
class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card")
```

```python
class UPIPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ${amount} using UPI")
```

```python
class PayPalPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ${amount} using PayPal")
```

---

## Step 3 - Context

```python
class PaymentService:

    def __init__(self, strategy):
        self.strategy = strategy

    def checkout(self, amount):
        self.strategy.pay(amount)
```

### Why is this called Context?

The Context is the class that **uses** a strategy.

It doesn't know *how* payment works.

It simply delegates the work to the selected strategy.

---

## Composition over Inheritance

Notice this line:

```python
self.strategy = strategy
```

This means **PaymentService HAS A PaymentStrategy**.

It does **not** inherit from `PaymentStrategy`.

This is called **Composition**.

### Why not Inheritance?

Inheritance represents an **IS-A** relationship.

For example:

```
Dog IS-A Animal
```

Composition represents a **HAS-A** relationship.

```
PaymentService HAS-A PaymentStrategy
```

Composition is preferred because you can change the strategy at runtime.

Today:

UPI

Tomorrow:

PayPal

Without changing `PaymentService`.

That's why people say:

> **"Favor Composition over Inheritance."**

---

## Programming to an Interface

Notice that `PaymentService` never knows whether it's using

* UPI
* Credit Card
* PayPal

It only knows

```python
PaymentStrategy
```

## Advantages

* Easy to add new payment methods
* No large if-else blocks
* Easy testing
* Better maintainability

---

## SOLID Principles

✅ Open Closed Principle

✅ Single Responsibility Principle

✅ Dependency Inversion Principle

✅ Liskov Substitution Principle

| Principle | Meaning                                               | Spotify Example                                                                                                |
| --------- | ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **OCP**   | Add new functionality without modifying existing code | Add `ApplePayPayment` as a new class instead of editing `PaymentService`.                                      |
| **SRP**   | One class should have one responsibility              | `UPIPayment` only handles UPI, `PayPalPayment` only handles PayPal.                                            |
| **DIP**   | Depend on abstractions, not concrete classes          | `PaymentService` depends on `PaymentStrategy`, not `UPIPayment`.                                               |
| **LSP**   | Child classes should be interchangeable               | `UPIPayment`, `PayPalPayment`, and `CreditCardPayment` can all be used wherever `PaymentStrategy` is expected. |


---

# Transition

Now ask another question.

We solved **how** payment happens.

But...

Who creates


Imagine Spotify has multiple places where users can make payments:

Premium Subscription Page
Family Plan Subscription
Student Premium Subscription
Gift Card Purchase
Podcast Subscription
Audiobook Purchase
Spotify Web
Spotify Mobile App

If every module needs to decide which payment object to create, developers might end up writing the same if-else logic in every place.


Let's solve that.

---

# 2. Factory Pattern

## Why is it called Factory?

Think about a real factory.

You don't build a car yourself.

You simply ask the factory.

The factory decides how to manufacture it.

Software factories do the same.

Instead of creating objects ourselves,

we ask the Factory to create them.

---

## Category

**Creational Design Pattern**

Creational patterns focus on **how objects are created.**

---

## Problem

Different pages in Spotify need payment strategies.

* Premium Page
* Family Plan
* Student Plan
* Gift Cards

Every page writes

```python
if payment == "upi":
    strategy = UPIPayment()

elif payment == "paypal":
    strategy = PayPalPayment()
```

Now the same code exists everywhere.

Duplication.

---

## Solution

Move object creation into one place.

```python
class PaymentFactory:

    @staticmethod
    def create(payment_type):

        if payment_type == "upi":
            return UPIPayment()

        elif payment_type == "credit":
            return CreditCardPayment()

        elif payment_type == "paypal":
            return PayPalPayment()

        raise Exception("Unsupported")
```

Usage

```python
strategy = PaymentFactory.create("upi")

payment = PaymentService(strategy)

payment.checkout(499)
```

---

## Terminology

**Factory**

Creates objects.

**Product**

The interface (`PaymentStrategy`).

**Concrete Product**

`UPIPayment`

`CreditCardPayment`

`PayPalPayment`

**Client**

The class requesting an object.

---

## Advantages

* Centralized object creation
* Cleaner client code
* Less duplication
* Easy maintenance

---

## SOLID

✅ OCP

✅ SRP

✅ DIP

---

# Transition

Payment completed successfully.

Now what?

Should PaymentService call

```python
send_email()

update_analytics()

reward_points()

push_notification()
```

Imagine tomorrow.

SMS

Slack

WhatsApp

Invoice Service

Now PaymentService becomes another God Class.

---

# 3. Observer Pattern

## Why is it called Observer?

Imagine you're watching a cricket match.

Whenever Virat Kohli hits a century,

millions of people watching celebrate immediately.

They are **observing** the match.

Similarly,

many services observe the Payment Service.

When payment succeeds,

everyone interested gets notified.

That's why it's called the **Observer Pattern**.

---

## Category

**Behavioral Design Pattern**

Behavioral patterns define

> **How objects communicate.**

---

## Solution

PaymentService simply announces

```
Payment Successful
```

Everyone listening reacts.

```
Payment Successful
        │
────────┼──────────
│       │        │
Email Analytics Rewards
```

---

## Observer Interface

```python
from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def update(self):
        pass
```

---

## Concrete Observers

```python
class EmailService(Observer):

    def update(self):
        print("Email Sent")
```

```python
class AnalyticsService(Observer):

    def update(self):
        print("Analytics Updated")
```

---

## Subject

```python
class PaymentService:

    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

    def complete_payment(self):
        print("Payment Successful")
        self.notify()


payment = PaymentService()

payment.subscribe(EmailService())
payment.subscribe(AnalyticsService())
payment.subscribe(RewardService())
```

---

## Why is this called Observer?

Because these services don't constantly ask:

> "Has payment completed?"

Instead, they **observe** the payment service.

When an event occurs,

they're notified automatically.

---

## Terminology

**Subject (Publisher)**

The object being observed.

**Observer**

Objects waiting for updates.

**Subscribe**

Register an observer.

**Notify**

Inform all observers.

**Event**

Something happened.

Example:

```
Payment Successful
```

---

## Advantages

* Loose coupling
* Easy to add new observers
* Highly scalable
* Cleaner code

---

## SOLID

✅ OCP

✅ SRP

✅ DIP

---

# 🎯 Final Picture

```
User clicks Buy Premium
        │
        ▼
Factory Pattern
Creates the correct Payment Strategy
        │
        ▼
Strategy Pattern
Processes payment using UPI / Credit Card / PayPal
        │
        ▼
Observer Pattern
Notifies Email, Analytics, Rewards, Notifications
```

---

