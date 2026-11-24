# One Emoji, One Dream Vacation

[![Competition](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![Rank](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/Joppy26/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/rank.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![Reward](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/Joppy26/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/reward.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)

Entry for the [One Emoji, One Dream Vacation bounty on make.fun](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35) ($2 winner-takes-all).

## The emoji

> 🌠

A shooting star. A dream vacation is not a beach, it is one night far from
city lights, lying back, catching a wish as it streaks across the dark.
Every other entry reaches for sun, sand or a plane; this one is the wish
itself, the exact moment that makes a stranger want to book the flight.

**Character count: 1** (limit 8). Verified by running `main.py` twice:
both runs produce byte-identical output.

## How it works

`main.py` (Python 3, standard library only, no network, no clock, no
randomness) writes the single emoji to `entry.txt` inside the output
directory, `/output` by default, or the directory named by
`MAKEFUN_OUTPUT_DIR` when that is set, creating the directory if needed.
Every run produces the exact same file.

## Run it

```sh
python3 main.py
```

or, to check the output locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/vacation-out python3 main.py
cat /tmp/vacation-out/entry.txt
```
