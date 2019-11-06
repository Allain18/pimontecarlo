"""Calcule pi grace à la méthode de monte Carlo"""

import random
import sys


def main(arg):
    """Fonction principale"""
    total = int(arg)
    inside = 0

    for _ in range(total):
        x_coord = random.random()
        y_coord = random.random()

        if (x_coord**2 + y_coord**2) < 1:
            inside += 1

    print(inside/total*4)


if __name__ == "__main__":
    main(sys.argv[1])
