#!/usr/bin/env python3
import pandas
from matplotlib.pyplot import figure, show, xkcd
from pathlib import Path

R = Path(__file__).parent

fn = R / "MacOShardware.csv"

dat = pandas.read_csv(fn, index_col=0, usecols=[0, 1, 2, 3, 4, 5, 6], skiprows=(1, 2))

with xkcd():
    fg = figure(figsize=(12, 5))
    axs = fg.subplots(1, 2, sharey=True)

    ax = axs[0]
    for k in ("Macbook", "Macbook Air", "Macbook Pro"):
        ax.plot(dat.index, dat[k].values, label=k, alpha=0.5, linestyle="--", marker="*")
    ax.tick_params(axis="x", labelrotation=20)
    ax.set_ylabel("year")
    ax.set_xlabel("MacOS version")
    ax.legend()

    ax = axs[1]
    for k in ("Mac Mini", "Mac Pro", "iMac"):
        ax.plot(dat.index, dat[k].values, label=k, alpha=0.5, linestyle="--", marker="*")
    ax.tick_params(axis="x", labelrotation=20)
    ax.legend()

    fg.suptitle("MacOS version vs. hardware requirements")

show()
