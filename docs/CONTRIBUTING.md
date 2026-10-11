# Introduction

_Hello, and welcome to the Algorithm Visualizer project! This document outlines the guidelines for contributing to the project. Thank you so much for taking the time to contribute; have fun!_
**Remember to go by PLAN.md for the project plan and roadmap**
**Update the docs as needed when making changes**

## Table of Contents

1. [Introduction](#introduction)
2. [Standards](#code-standards-and-best-practices)
3. [Data Flow](#data-flow)
4. [Testing](#testing)
5. [Commit Messages](#commit-messages)

## Code Standards and Best Practices

- Follow existing code style and conventions (unless there is a good reason to deviate).
- Use clear and descriptive variable and function names.
- Write modular and reusable code.
- Separate concerns by layers.
- Docstring at the top of each file and function to explain its purpose and usage.
- Type hints used for function parameters and return types.
- Use Optional[type] for functions that can return None
- In most cases, functions should not exceed ~25 lines
- Avoid using global variables unless absolutely necessary.

## Data Flow

- Allow data to flow through the system in a clear and predictable manner.
- Layers should not mix
- Avoid circular dependencies between modules.
- Allow docstrings to describe where the data is coming from and where it is going to.

## Testing

- Write tests as you write the functions
- Utilize fixtures
- Make sure you are asserting important info, not something like a "success" message
- Use the test database for testing
- Don't be afraid to comment.

## Commit Messages

- Use clear and descriptive commit messages.
- Try not to let a commit exceed 2 sentences, if so, try separating commits.
- Commit after completing a logical unit of work.
- Push after each commit.
- Be straight-to-the-point and concise
- Reference completing part of the checklist if done. It's preferred if you literally "x" it off in PLAN.md.
- Communicate the version (+0.1 for a new feature/milestone, + 0.0.1 for a bug fix, +1.0 for a rework/finished release) in the commit message if your code addition is a new feature or milestone.
