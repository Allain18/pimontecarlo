"""Calcule pi grace à la méthode de monte Carlo"""

import random
import argparse


def compute_pi(iteration, show_plot):
    """Compute pi"""

    assert isinstance(iteration, int)
    inside = 0

    for _ in range(iteration):
        x_coord = random.random()
        y_coord = random.random()

        if (x_coord**2 + y_coord**2) < 1:
            inside += 1

    pi_aprox = inside/iteration*4

    return pi_aprox


def get_argument():
    """
    Get the command line argument
    Number of iterations to compute pi
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "iteration", help="number of iterations to compute pi", type=int)
    parser.add_argument(
        "-p", "--plot", help="Show the position of the point", action="store_true")
    args = parser.parse_args()

    return args


def main():
    """
    Entry point for command line
    """
    arg = get_argument()
    iteration = arg.iteration
    show_plot = arg.plot
    compute_pi(iteration, show_plot)


if __name__ == "__main__":
    main()
