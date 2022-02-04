import numpy as np


def spline1(x, knots, Dy1=None, Dyk=None):

    x = np.asarray([x])
    # print("x:", x, x.shape)
    nx = x.shape[0]
    nk = knots.shape[0]
    y = np.zeros((nx, 1))
    dy = y
    # print(len(y))
    index = np.zeros((nx, 1))

    if Dy1 is None:
        Dy1 = 0
    if Dyk is None:
        Dyk = 0

    Dy = np.divide(
        (knots[1:nk, 1]-knots[0:nk-1, 1]),
        (knots[1:nk, 0]-knots[0:nk-1, 0])
        )
    Dy = np.concatenate((Dy, np.array([0])))

    for i in range(nx-1):
        j = 1
        while x[i] > knots[np.min(nk, j-1), 0] and j <= nk:
            j += 1
        j -= 1

        if j == 0:
            y[i] = knots[0, 1] - Dy1 * (knots[0, 0]-x[i])
            dy[i] = Dy1

        else:
            y[i] = knots[j-1, 1] - Dy[j-1] * (knots[j-1, 0] - x[i])
            dy[i] = Dy[j-1]

        index[i-1] = j-1
    print(y)

    return y #, dy, index