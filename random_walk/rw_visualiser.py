import random
from matplotlib import pyplot as plt

plot = False  # to run plots type True


def random_walk_visualiser(n):
    """ Random walks generator in terms of n == number of blocks
        It has 4 more directions including diagonal paths. """

    x, y = 0, 0
    x_cont, y_cont = [0], [0]
    for i in range(n):
        dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0),
                                (1, 1), (-1, 1), (-1, -1), (1, -1)])
        x += dx
        y += dy
        x_cont.append(x)
        y_cont.append(y)
    return x_cont, y_cont


""" All the plotting part of the random walk """

if plot:
    fig = plt.figure()
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    plt.xlim(-25, 25)
    plt.ylim(-25, 25)
    ax.axes.xaxis.set_ticklabels([])
    ax.axes.yaxis.set_ticklabels([])
    # ax.grid(True)
    for i in range(1, 31):
        test_walk = random_walk_visualiser(50)
        x_coordinates = test_walk[0]
        y_coordinates = test_walk[1]
        ax.plot(x_coordinates, y_coordinates)
    plt.show()
