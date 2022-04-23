def make_graph(xs, ys, filename):
    from matplotlib import pyplot as plt

    fig = plt.figure()
    plt.plot(xs, ys)
    fig.savefig(filename)

    return