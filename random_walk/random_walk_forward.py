import random
from matplotlib import pyplot as plt

""" Simulates a random walk where the choice never goes back to the previous position.
    I understand it takes away a bit of the randomness, but I thought it was a good
    exercise to try recursion. """

global_coordinates = [(0, 0)]
plot = True  # to run plots type True


def random_walk_forward(n, tmp_x=0, tmp_y=0, x=0, y=0):
    """ Generates coordinates for random walks in the order of n without the option of
        using the previous movement.Therefore, it is randomly moving forward via 8 directions:
        including lateral, up&down and diagonal paths. """

    global global_coordinates
    if n == 0:
        return
    for i in range(n):
        dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0),
                                (1, 1), (-1, 1), (-1, -1), (1, -1)])
        # print((dx, dy), 'dx -- dy') /// Debugging option
        # print((tmp_x, tmp_y), 'tmp_x -- tmp_y') /// Debugging option
        if (tmp_x + dx) == 0 and (tmp_y + dy) == 0:
            random_walk_forward(n-i, tmp_x, tmp_y, x, y)
            return
        tmp_x = dx
        tmp_y = dy
        x += dx
        y += dy
        global_coordinates.append((x, y))
        # print(i, 'simulation ==>', (x, y)) /// Debugging option
        # print(10*'---') /// Debugging option


""" For plotting the random walk """


def plot_it(plots=False):
    global global_coordinates

    if not plots:
        for each in global_coordinates:
            print("[{}]".format(each))

    # print(global_coordinates) /// Debugging option
    else:
        x_walk = []
        y_walk = []
        for xs, ys in global_coordinates:
            x_walk.append(xs)
            y_walk.append(ys)

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
        ax.plot(x_walk, y_walk, 'r-o')
        plt.show()


def main():
    random_walk_forward(50)  # number of blocks
    plot_it(plot)


if __name__ == '__main__':
    main()
