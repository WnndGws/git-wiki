---
title: 0004_using-git-crypt
author: Wynand Gouws
date: 2024-12-09T15:25:31.000Z
public: true
---

- Seems like order of operations matters a lot

- While in folder you want to commit:

```zsh
git init
git-branchless init
cp ~/.gitattributes .
git-crypt unlock /path/to/file
git-crypt status -f
git add .
git commit -m 'message'
git-crypt lock
git-crypt unlock /path/to/file
gh repo create
git push
```
