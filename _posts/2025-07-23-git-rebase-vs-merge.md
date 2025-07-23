---
title: "Git Rebase vs Merge"
tags: 
    - git
    - version control
    - software development
---

If you’ve worked with Git for even a short while, you’ve probably encountered two powerful commands: `merge` and `rebase`. Both are used to integrate changes from one branch into another — but they do so in fundamentally different ways.

In this blog, we’ll break down:

- What `git merge` and `git rebase` do
- How they differ (with visual examples)
- When to use each (and why it matters)

## What Is `git merge`

`git merge` takes the contents of one branch and integrates it into another. It creates a new **merge commit** that ties together the histories of both branches.

### Example

```bash
git checkout main
git merge feature-branch

This will generate a new commit like:

*   d4e3f5d (main) Merge branch 'feature-branch'
|\
| * 73ca1a3 (feature-branch) Add new feature
* | 12a8b6f Previous main commit
|/
```

✅ Pros:

- Preserves the full history of commits
- Shows a complete picture of how branches developed
- Safer and easier for teams to collaborate

❌ Cons:

- Can clutter the log with unnecessary merge commits
- Makes the commit history non-linear and harder to follow

## What Is `git rebase`

`git rebase` moves or “replays” the commits from one branch onto another, as if they were created there originally. It avoids merge commits by rewriting history.

Example:

git checkout feature-branch
git rebase main

This changes the base of feature-branch to the tip of main:

- 95fb0c3 (feature-branch) Add new feature
- 12a8b6f (main) Previous main commit

✅ Pros:

- Creates a clean, linear commit history
- Easier to follow with tools like git log or git bisect
- Useful for preparing pull requests

❌ Cons:

- Rewrites commit history (can be dangerous if used improperly)
- Not safe for branches that are shared with others (can cause conflicts and confusion)

## Merge vs Rebase: A Visual Summary

Let’s say you start with this:

```plaintext
main:    A---B---C
                  \
feature:           D---E


# **Merge** creates a new commit F:

main:    A---B---C-------F
                       /   \
feature:              D —– E

# **Rebase** moves `D` and `E` on top of `C`:

main:    A—B—C—D’—E’
```

## When to Use Each

| Scenario                         | Use `merge`                         | Use `rebase`                      |
|----------------------------------|-------------------------------------|----------------------------------|
| Collaborating on shared branches | ✅ Yes                              | 🚫 Avoid (unless everyone agrees) |
| Cleaning up commit history       | 🚫 May create noise                 | ✅ Great for a tidy history       |
| Preparing for pull requests      | ✅ Fine                             | ✅ Preferred by many              |
| Wanting to preserve history      | ✅ Keeps all original commits       | 🚫 Rewrites history               |

## Best Practices

- Use **merge** when working with others to maintain a complete and safe history.
- Use **rebase** before merging your own feature branch, to squash and clean up commits.
- **Never rebase public branches** (i.e., ones shared with others) unless you know what you're doing.
