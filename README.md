📘 Social Network – “People You May Know” Logic
🚀 From Confusion to Clarity

This project represents my journey from not understanding basic JSON structures to successfully building a working “People You May Know” recommendation system using Python.

When I started, I was confused about:

The difference between list index and user ID

How dictionaries work

Why we need a lookup map

Why loops were necessary

What .get() actually does

How nested loops connect logic together

Through repeated practice and debugging, I broke down each concept and rebuilt it step by step.

🧠 What I Learned
1️⃣ JSON → Python Conversion

I learned that:

JSON objects become Python dictionaries

JSON arrays become Python lists

The users data is a list of dictionaries, not a dictionary itself.

2️⃣ List vs Dictionary Difference

users → a list (accessed by index like users[0])

user → a dictionary (accessed by key like user["id"])

The index 0 is just position.
The "id" field is the actual identity of the user.

3️⃣ Why We Build user_map

Instead of searching through the full list every time, we build a lookup dictionary:

user_map[user["id"]] = user

This allows instant access:

user_map[5]

That reduces search time and makes the logic efficient.

4️⃣ Core Logic – Friends of Friends

The recommendation system works like this:

Take one user.

Look at their friends.

For each friend:

Look at that friend's friends.

If a person is:

Not the current user

Not already a friend
→ Add them to suggestions.

This is essentially a depth-2 graph traversal.

User → Friend → Friend's Friend

5️⃣ Why We Use a Set
suggest = set()

Sets:

Automatically prevent duplicates

Allow fast membership checking

Make filtering efficient

6️⃣ Why We Use .get()
friend = user_map.get(friend_id)

.get() safely retrieves data without crashing if the key does not exist.

It prevents runtime errors and makes the program more stable.

7️⃣ Final Output Logic

If suggestions exist:

Loop through IDs

Convert ID → user dictionary

Extract name

Print

If empty:

Print "none"

💡 What Changed for Me

At first, I tried to memorize lines.

Later I understood:

Don’t memorize syntax.
Understand the story behind the logic.

Once the structure made sense, the code became easy to rebuild.

🎯 What This Project Represents

This project shows growth in:

Understanding data structures

Working with nested dictionaries

Graph-like thinking

Debugging syntax errors

Managing indentation properly

Translating logic into working code

It started with confusion about IDs and indexing.
It ended with confidently writing a full recommendation system from scratch.

🔥 Final Realization

Practice builds fluency.

Understanding builds confidence.

Rewriting builds mastery.
