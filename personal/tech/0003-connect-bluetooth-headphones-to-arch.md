---
title: 0003-connect-bluetooth-headphones-to-arch
author: Wynand Gouws
date: 2026-05-22 13:39:15
public: true
---

# Connecting process

```zsh
bluetoothctl connect 00:04:32:9A:8E:96
pactl set-default-sink bluez_output.00_04_32_9A_8E_96.1
```

| device|mac|
|--|--|
| Atlas Air | 00:04:32:9A:8E:96

---
