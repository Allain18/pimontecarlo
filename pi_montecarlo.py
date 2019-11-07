"""Calcule pi grace à la méthode de monte Carlo"""

import random
import argparse


def compute_pi(iteration):
    """Compute pi"""

    inside = 0

    for _ in range(iteration):
        x_coord = random.random()
        y_coord = random.random()

        if (x_coord**2 + y_coord**2) < 1:
            inside += 1

    print(inside/iteration*4)


def get_argument():
    """
    Get the command line argument
    Number of iterations to compute pi
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "iteration", help="number of iterations to compute pi", type=int)
    args = parser.parse_args()

    return args


def main():
    """
    Entry point for command line
    """
    iteration = get_argument().iteration
    compute_pi(iteration)


if __name__ == "__main__":
    main()
