# Scissors Paper Rock Expert System

It is a simple expert system implementation of an ES playng scissors paper rock game.

## How to play:

```bash
python main.py [--debug]
```

Then follow messgaes on screen.
First two round the computer will choose randomly. From round 3, the ES will try to predict your choice using your two latest choices.
The more you play more the ES will learn about you.

If you use the `--debug` option you will see the rules decicion table:

``` python
╒═══════════════╤═════════════════════════╤══════════════╤══════════╤═════════╕
│ Last Choice   │ Second to Last Choice   │ Consequent   │   Weight │ Valid   │
╞═══════════════╪═════════════════════════╪══════════════╪══════════╪═════════╡
│ STONE         │ STONE                   │ STONE        │       -2 │ True    │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ STONE         │ STONE                   │ PAPER        │       -1 │ True    │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ STONE         │ STONE                   │ SCISSORS     │        1 │ True    │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ STONE         │ PAPER                   │ STONE        │       -1 │ False   │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ STONE         │ PAPER                   │ PAPER        │        1 │ False   │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ STONE         │ PAPER                   │ SCISSORS     │        0 │ False   │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ STONE         │ SCISSORS                │ STONE        │       -1 │ False   │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ STONE         │ SCISSORS                │ PAPER        │        0 │ False   │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ STONE         │ SCISSORS                │ SCISSORS     │        0 │ False   │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ PAPER         │ STONE                   │ STONE        │        0 │ False   │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ PAPER         │ STONE                   │ PAPER        │        0 │ False   │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ PAPER         │ STONE                   │ SCISSORS     │        0 │ False   │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ PAPER         │ PAPER                   │ STONE        │        0 │ False   │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ PAPER         │ PAPER                   │ PAPER        │        0 │ False   │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ PAPER         │ PAPER                   │ SCISSORS     │        0 │ False   │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ PAPER         │ SCISSORS                │ STONE        │        0 │ False   │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ PAPER         │ SCISSORS                │ PAPER        │        0 │ False   │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ PAPER         │ SCISSORS                │ SCISSORS     │        0 │ False   │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ SCISSORS      │ STONE                   │ STONE        │       -1 │ False   │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ SCISSORS      │ STONE                   │ PAPER        │        0 │ False   │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ SCISSORS      │ STONE                   │ SCISSORS     │        0 │ False   │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ SCISSORS      │ PAPER                   │ STONE        │        0 │ False   │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ SCISSORS      │ PAPER                   │ PAPER        │        0 │ False   │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ SCISSORS      │ PAPER                   │ SCISSORS     │        0 │ False   │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ SCISSORS      │ SCISSORS                │ STONE        │        0 │ False   │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ SCISSORS      │ SCISSORS                │ PAPER        │        0 │ False   │
├───────────────┼─────────────────────────┼──────────────┼──────────┼─────────┤
│ SCISSORS      │ SCISSORS                │ SCISSORS     │        0 │ False   │
╘═══════════════╧═════════════════════════╧══════════════╧══════════╧═════════╛
```
It is used to predict the next user choice. As this is a simple and known domain we are able to define and see the entire rules table.

This was inpired by the book **Inteligencia Artificial** `ISBN 978-987-1347-51-3`
