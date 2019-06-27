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

TL;DR, Run this with python2.
```sh
python2 chals.py # build database
python2 run.py # run
```

## Screenies
![home](/screenshot/home.png)
![chall](/screenshot/chall.png)
![score](/screenshot/score.png)

## Score policy
- No first blood.
- Dynamic Scoring, all the challenges start with the same points, more solves, fewer points.
- If two players have the same score the rank is computed looking at the last submission time.

## credits
[motherfucking-ctf](https://github.com/andreafioraldi/motherfucking-ctf)