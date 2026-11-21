# AGENTS.md — tiny-chess-01 entry

This repository is an entry for the make.fun bounty "tiny-chess-01":
the strongest chess engine that fits in 4,096 bytes of Python.

## What to build

- `main.py` at the repository root is the whole engine.
  - At most 4,096 bytes as committed (comments and whitespace count).
  - Python 3.13, standard library only. It reads, imports or runs no other file.
  - It talks to the game environment over HTTP at `$MAKEFUN_ENV_URL`
    (POST /game, /move, /resign with JSON bodies). The exact protocol is in the
    kit's `practice/trial-0/input/prompt.txt` and `RULES.txt`
    (kit: `~/workspace/makefun-exp/work/tiny-chess-01-kit/`).
- The engine must be an original implementation. Standard techniques are fine
  (negamax with alpha-beta, quiescence search, MVV-LVA ordering, piece-square
  tables), but never copy or port an existing engine's code.
- Deterministic: search to a fixed depth or a fixed node budget, never to a
  clock. No unseeded randomness, no dependence on hash iteration order.
- Speed: a move must stay well inside the 10 second move limit on 1 CPU;
  target at most ~2 seconds per move when measured locally.

## Workflow

- Build in steps: write a first working version, test it locally, then improve
  it in a second version. Commit each version separately.
- After each commit, push to GitHub with `../push_github.py`.
- Local tests: check move legality on known positions (perft on the start
  position), measure per-move time, and if possible run the kit's local grader:
  `node cli/makefun.mjs grade-local --kit . --bot <this repo> --driver process`
  from inside the kit directory.
- Keep the repository slim: `main.py`, `LICENSE`, `README.md`, `AGENTS.md` only.
  Test scripts live outside the repository.

## Do not

- Do not submit the entry to make.fun. Building and pushing only.
- Do not add model/API calls to the engine. That disqualifies the entry.
