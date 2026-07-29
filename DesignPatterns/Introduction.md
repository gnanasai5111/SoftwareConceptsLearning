# Design Patterns

---

# 1. Imagine Building Spotify 🎵

Imagine you're a software engineer, and your manager asks you to build a simple music streaming application like **Spotify**.

Initially, your application has only one feature:

* Play Music

The codebase is small—maybe around **100 lines of code**. Everything is simple, easy to understand, and adding new features takes only a few minutes.

At this stage, you don't think much about software architecture or Design Patterns because there isn't enough complexity to justify them.

So naturally, you might ask:

> **"If my application already works, why would I need Design Patterns?"**

That's a valid question.

The truth is, **you probably don't need them on day one.**

The real challenge begins when your application starts growing.

> 💡 **Key Point:** Design Patterns are not created for small applications. They become valuable as software grows in size and complexity.

---

# 2. It Works... At First... Until It Doesn't ❌

As your application becomes popular, users start requesting more features.

Your product team decides to add:

* Search Songs
* Premium Subscription
* Playlist Support
* Offline Downloads
* Song Recommendations
* Notifications
* Analytics
* Advertisements

To deliver these features quickly, you keep adding everything to the same class.

```python
class SpotifyManager:

    def play_song(self):
        pass

    def process_payment(self):
        pass

    def search_song(self):
        pass

    def create_playlist(self):
        pass

    def download_song(self):
        pass

    def recommend_song(self):
        pass

    def send_notification(self):
        pass

    def generate_analytics(self):
        pass
```

At first, this doesn't seem like a problem.

Everything is in one place, the application still works, and adding new functionality feels easy.

However, after a few months, your project grows from **100 lines** to **10,000 or even 100,000 lines of code**.

Now:

* More developers join the team.
* New features are released every sprint.
* Bugs need to be fixed regularly.
* Existing features require continuous improvements.

### A New Business Requirement

Imagine your business team now wants to support multiple payment methods.

Currently, Spotify only supports **Credit Cards**.

Now you need to add:

* UPI
* PayPal
* Apple Pay
* Google Pay
* Net Banking

At first, this sounds like a simple change.

But once you start working on it, you realize it affects multiple parts of the application.

You need to modify:

* Payment Logic
* Subscription Validation
* Invoice Generation
* Notifications
* Analytics

A feature that looked simple now requires changes across multiple modules.

Developers begin asking an important question:

> **"Why does one small feature require changes everywhere?"**

This is a clear sign of **poor software design**.

The `SpotifyManager` class has become responsible for too many things. Such a class is commonly called a **God Class** because it tries to do everything.

### Problems with This Approach

* One class has too many responsibilities.
* The code becomes difficult to understand.
* Testing becomes harder.
* Every new feature increases complexity.
* Multiple developers working on the same file can lead to merge conflicts.
* Small changes can accidentally break existing functionality.

> 💡 **Key Point:** The application still works, but maintaining and extending it becomes increasingly difficult.

---

# 3. What is Software Design? 🏗️

If poor design creates these problems, how can we avoid them?

The answer is **Software Design**.

Software Design is the process of deciding **how different parts of an application are organized and how they communicate with each other.**

Before writing code, we answer questions like:

* Which class should play music?
* Which class should handle payments?
* Which class should send notifications?
* How should different components communicate?

These decisions determine how maintainable, scalable, and flexible the application will be.
---

# 4. A Better Design ✅

Instead of placing everything inside one class, divide responsibilities.

```text
SpotifyApplication
│
├── PlayerService
├── PaymentService
├── SearchService
├── RecommendationService
├── NotificationService
└── AnalyticsService
```

Now every class has a single, well-defined responsibility.

| Class                 | Responsibility                    |
| --------------------- | --------------------------------- |
| PlayerService         | Play music                        |
| PaymentService        | Handle subscriptions and payments |
| SearchService         | Search songs and artists          |
| RecommendationService | Recommend songs                   |
| NotificationService   | Send notifications                |
| AnalyticsService      | Generate reports and analytics    |

### Benefits

* Easier to understand.
* Easier to test.
* Easier to maintain.
* Easier to extend with new features.
* Allows multiple developers to work on different modules independently.

Notice that we still haven't talked about Design Patterns.

We've simply learned what **good software design** looks like.

---

# 5. Recurring Problems 🔄

As software systems became larger, companies around the world started facing similar design challenges.

Questions like:

* How should objects be created?
* How can I change behavior without modifying existing code?
* How can different classes communicate without becoming tightly coupled?
* How can I reuse successful designs?

Companies like **Google, Netflix, Amazon, and Spotify** all faced these problems.

Although they built different products, many of the underlying design challenges were surprisingly similar.

Developers realized they were solving the same problems repeatedly.

Instead of reinventing solutions every time, they documented the approaches that consistently worked well.

These proven solutions became known as **Design Patterns**.

---

# 6. What is a Design Pattern? 🧩

A **Design Pattern** is a **proven, reusable solution to a recurring software design problem.**

Let's break this definition into smaller parts.

### Proven

The solution has been tested and successfully used by thousands of developers over many years.

### Reusable

The same idea can be applied to many different projects.

### Recurring Problem

A problem that appears repeatedly during software development.

### Solution

A general approach or blueprint for solving the problem.

A Design Pattern is **not**:

* A programming language
* A framework
* A library
* Copy-paste code

Instead, it is a **blueprint** that helps developers solve common design problems.

---

# 7. Gang of Four (GoF) 📘

In 1994, four software engineers published one of the most influential books in software engineering:

**Design Patterns: Elements of Reusable Object-Oriented Software**

The authors were:

* Erich Gamma
* Richard Helm
* Ralph Johnson
* John Vlissides

Together, they became popularly known as the **Gang of Four (GoF).**

Their book documented **23 Design Patterns**, many of which are still widely used today.

---

# 8. Categories of Design Patterns 📂

The 23 GoF Design Patterns are grouped into three categories.

## 1. Creational Patterns

Focus on **how objects are created**.

Examples:

* Factory Method
* Abstract Factory
* Builder
* Singleton

## 2. Structural Patterns

Focus on **how classes and objects are organized**.

Examples:

* Adapter
* Decorator
* Facade
* Composite

## 3. Behavioral Patterns

Focus on **how objects communicate and interact**.

Examples:

* Strategy
* Observer
* Command
* State

Think of these categories as answering three questions:

* **Creational** → How should objects be created?
* **Structural** → How should objects be connected?
* **Behavioral** → How should objects communicate?

For this session, we'll focus on:

* ✅ Strategy Pattern
* ✅ Factory Pattern
* ✅ Observer Pattern


