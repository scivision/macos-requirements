#!/usr/bin/env python3
# /// script
# dependencies = [
# "pandas",
# "matplotlib",
# ]
# ///

import typing
from pathlib import Path

import pandas
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

R = Path(__file__).parent

fn = R / "macOShardware.csv"

dat = pandas.read_csv(fn, index_col=0, skiprows=(1, 2, 3, 4, 5))

with plt.xkcd():
    fg = plt.figure(figsize=(12, 5), layout="constrained")
    axs: typing.Any = fg.subplots(1, 2, sharey=True)

    ax = axs[0]
    for k in {"Macbook Air", "Macbook Pro", "Macbook Neo"}:
        ax.plot(
            dat.index, dat[k].values, label=k, alpha=0.5, linestyle="--", marker="*"
        )
    ax.tick_params(axis="x", labelrotation=20)
    ax.set_ylabel("year")
    ax.set_xlabel("macOS version")
    ax.legend()

    ax = axs[1]
    for k in {"Mac Studio", "Mac Mini", "Mac Pro", "iMac"}:
        ax.plot(
            dat.index, dat[k].values, label=k, alpha=0.5, linestyle="--", marker="*"
        )
    ax.tick_params(axis="x", labelrotation=20)
    ax.legend()

    fg.suptitle("macOS version vs. hardware required")

    fg = plt.figure(constrained_layout=True)
    ax = fg.gca()
    ax.set_ylabel("year")
    ax.set_xlabel("macOS version")
    ax.set_title("macOS version vs. End of Life")
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    ax.plot(
        dat.index,
        dat["EOL"].values,
        linestyle="--",
        marker="*",
        color="red",
    )

plt.show()
