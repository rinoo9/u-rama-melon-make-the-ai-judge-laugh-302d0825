[![Make the AI Judge Laugh](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![Rank](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/rinoo9/u-rama-melon-make-the-ai-judge-laugh-302d0825/rank.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![Reward](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/rinoo9/u-rama-melon-make-the-ai-judge-laugh-302d0825/reward.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825)

# Make the AI Judge Laugh

An entry for the [make.fun](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825) bounty **"Make the AI Judge Laugh"**.

## The entry

> HR said to treat the office like family, so I asked my manager for my allowance and got sent to my room.

Take "we're a family here" literally and the office turns into a household: the manager owes you an allowance, and asking for it gets you sent to your room like a grounded kid.

## How it works

`main.py` is a deterministic program that writes exactly one line — the office-life joke above, within the 1–200 character gate — to `/output/entry.txt`. Before writing, it checks the line against the gate itself (non-blank, one line, 1–200 characters) and exits with an error instead of shipping a line the gate would refuse. No network, no randomness, no environment input: the same line every run.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
