"""Calcule pi grace à la méthode de monte Carlo"""

import random
import argparse
import matplotlib.pyplot as plt


def compute_pi(iteration, show_plot=False):
    """Compute pi"""

    inside = 0
    x_inside = []
    y_inside = []

    x_outside = []
    y_outside = []

    for _ in range(iteration):
        x_coord = random.random() * 2 - 1
        y_coord = random.random() * 2 - 1

        if (abs(x_coord)**2 + abs(y_coord**2)) < 1:
            x_inside.append(x_coord)
            y_inside.append(y_coord)
            inside += 1
        else:
            x_outside.append(x_coord)
            y_outside.append(y_coord)

    pi_aprox = inside/iteration*4

    if show_plot:
        fig = plt.figure(num="Pi")
        axe = fig.add_subplot(1, 1, 1)
        axe.set_aspect(aspect=1)
        axe.set_xlim(-1, 1)
        axe.set_ylim(-1, 1)

        axe.plot(x_inside, y_inside, "bo")
        axe.plot(x_outside, y_outside, "ro")

        circle = plt.Circle((0, 0), 1, color="g")
        axe.add_artist(circle)

        axe.set_xlabel("pi = {}".format(pi_aprox))

        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
        plt.show()

    else:
        print(pi_aprox)

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
