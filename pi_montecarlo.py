"""Calcule pi grace à la méthode de monte Carlo"""

import random
import argparse
import matplotlib.pyplot as plt


def compute_pi(iteration, show_plot):
    """Compute pi"""

    assert isinstance(iteration, int)
    inside = 0
    x_inside = []
    y_inside = []

    x_outside = []
    y_outside = []

    for _ in range(iteration):
        x_coord = random.random()
        y_coord = random.random()

        if (x_coord**2 + y_coord**2) < 1:
            x_inside.append(x_coord)
            y_inside.append(y_coord)
            inside += 1
        else:
            x_outside.append(x_coord)
            y_outside.append(y_coord)

    pi_aprox = inside/iteration*4

    if show_plot:
        plt.figure(num="Pi")
        plt.title("Pi")
        plot = plt.gca()
        plot.set_xlim(0, 1)
        plot.set_ylim(0, 1)
        plot.plot(x_inside, y_inside, "bo")
        plot.plot(x_outside, y_outside, "ro")

        plt.xlabel("pi = {}".format(pi_aprox))
        plt.show()

    else:
        print(pi_aprox)


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
