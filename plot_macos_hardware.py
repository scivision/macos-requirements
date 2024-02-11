#!/usr/bin/env python3

import typing
from pathlib import Path

import pandas
from matplotlib.pyplot import figure, show, xkcd

R = Path(__file__).parent

fn = R / "macOShardware.csv"

dat = pandas.read_csv(fn, index_col=0, usecols=[0, 2, 3, 4, 5, 6], skiprows=(1, 2, 3))

with xkcd():
    fg = figure(figsize=(12, 5))
    axs: typing.Any = fg.subplots(1, 2, sharey=True)

    ax = axs[0]
    for k in {"Macbook Air", "Macbook Pro"}:
        ax.plot(dat.index, dat[k].values, label=k, alpha=0.5, linestyle="--", marker="*")
    ax.tick_params(axis="x", labelrotation=20)
    ax.set_ylabel("year")
    ax.set_xlabel("macOS version")
    ax.legend()

    ax = axs[1]
    for k in {"Mac Mini", "Mac Pro", "iMac"}:
        ax.plot(dat.index, dat[k].values, label=k, alpha=0.5, linestyle="--", marker="*")
    ax.tick_params(axis="x", labelrotation=20)
    ax.legend()

    fg.suptitle("macOS version vs. hardware required")

show()
