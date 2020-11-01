import random
from matplotlib import pyplot as plt

plot = False  # to run with plotting type True


def random_walk(n):
    """ Random walks generator in terms of n == number of blocks """

    x, y = 0, 0
    for i in range(n):
        dx, dy = random.choice([(0, 1), (0, -1), (-1, 0), (1, 0)])
        x += dx
        y += dy
    return x, y


""" -- Monte Carlo Simulation -- """

number_of_walks = 10000  # number of simulations

longest_walk = {}
walks_avg_distance = {}
walks_ratio = []
probability_list = []
avg_distance = 0
for walks in range(1, 31):  # number of blocks
    no_transport = 0
    for s in range(number_of_walks):
        walk = random_walk(walks)
        distance = abs(walk[0]) + abs(walk[1])
        avg_distance += distance
        if distance <= 4:
            no_transport += 1
    avg_distance = avg_distance/number_of_walks
    walks_avg_distance[walks] = round(avg_distance, 3)
    probability = float(no_transport/number_of_walks)*100
    probability_list.append(round(probability, 3))
    walks_ratio.append(round(avg_distance/walks, 3))

    """ Find the longest random walk with an average (50/50) of no transport """

    if probability > 50:
        longest_walk = {walks: probability}
    if not plot:
        print("{} blocks -- The average distance ==> {}".format(walks, round(avg_distance, 3)))
        print("{} yields a % of {}".format(walks, round(probability, 3)))
        print("--" * 23)

if not plot:
    print("The longest walk with a 50/50 chance of not having to take transportations is", longest_walk)

""" Plot the average distance, the ratio of distance and blocks 
    and the probability of no transport """

if plot:
    x, y = zip(*walks_avg_distance.items())
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    plt.figure(figsize=(12, 6))
    ax1.set_title("Average Distance/Number of Blocks")
    ax1.plot(x, y)
    ax2.set_title("Walk/Number of Blocks - Ratio")
    ax2.plot(x, walks_ratio)
    ax3.set_title("Probability/Number of Blocks")
    ax3.plot(x, probability_list)
    plt.show()
