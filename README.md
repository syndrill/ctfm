# CTFm
CTFd is a meme. Tuning up for simple auth extension is hard.
Here, I present you, the CTF-~~meme~~mini

**Why?** We need this for the lulz.

## Overview
- Define a description of the CTF in `templates/index.html`.
- Define the set of challenges in `./chals` directory. `.json` example included.
- Run `python chals.py` to setup the chals database.
- Run `python run.py` and you are up.
<!-- On Heroku, you should only enable the Heroku Postgres extension. -->

## Score policy
- I don't like the CTFs that benefit players depending on the timezone, so there isn't first blood.
- All the challenges start with the same points. More solves, fewer points. This choice let the users define the difficulty of a challenge.
- If two players have the same score the rank is computed looking at the last submission time.

## credits
[motherfucking-ctf](https://github.com/andreafioraldi/motherfucking-ctf)