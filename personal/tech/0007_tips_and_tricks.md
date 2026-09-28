---
title: 0008-tips-and-tricks
author: Wynand Gouws
date: 2026-09-05 09:04:36
public: true
---

# Tips and Tricks
* A series of interesting Linux/zsh/etc tips picked up along the way

## SSH
### SSH Shortcuts [^1]
* Add the something like these to be able to `ssh tiger` or `ssh tiger-t`
```~/.ssh/config
# Server I want to connect to
Host tiger*
    Hostname tiger.princeton.edu
    User kl5675

# Tunnel that I might use sometimes
Host tigressgateway
    Hostname tigressgateway.princeton.edu
    User kl5675

Host *-t
    ProxyJump tigressgateway

```

## ZSH
* Terminal command `fc` opens the last run command in `$EDITOR`

# References
* [1]:
  Everything* you didn't know you needed, Cited 2026-09-05, Available from
  [Link](https://klieret.github.io/everything-you-didnt-now-you-needed/3?clicks=1)
