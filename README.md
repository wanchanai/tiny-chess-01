# tiny-chess-01

A chess engine in at most 4,096 bytes of Python (`main.py`), built by an AI
agent for the make.fun bounty "Build the strongest chess engine in 4 KB of
Python".

The engine plays a gauntlet of house engines over HTTP: it reads the current
game from the environment at `$MAKEFUN_ENV_URL`, computes its move with a
fixed-node negamax search (alpha-beta, quiescence, MVV-LVA ordering,
piece-square tables), and posts the move back in UCI notation. It is fully
deterministic: same position, same move.

## Run

The grader runs it as `python3 main.py` with `MAKEFUN_ENV_URL` set to the
game environment. See `AGENTS.md` for the build rules.

## License

MIT — see `LICENSE`.
