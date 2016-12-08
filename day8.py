import numpy as np

from load_data import load_data


def _rect(X, w, h):
    for j in range(h):
        for k in range(w):
            X[j, k] = 1
    return X


def _rotateRow(X, idx, N):
    newcolidx = [(j - N) % X.shape[1] for j in range(X.shape[1])]
    X[idx, :] = X[idx, newcolidx]
    return X


def _rotate(X, rc, idx, N):
    if rc == 'row':
        X = _rotateRow(X, idx, N)
    elif rc == 'column':
        X = _rotateRow(X.T, idx, N).T
    else:
        raise Exception('parse error; expected row or column')
    return X


def updateDisplay(X, op):
    # X is a matrix of 0's and 1's
    # op is the operation to perform on X
    cmd = op.split(' ')
    if cmd[0] == 'rotate':
        idx = int(cmd[2][2:])
        N = int(cmd[-1])
        X = _rotate(X, cmd[1], idx, N)
    elif cmd[0] == 'rect':
        whsep = cmd[1].index('x')
        w = int(cmd[1][:whsep])
        h = int(cmd[1][(whsep+1):])
        X = _rect(X, w, h)
    else:
        print(X)
        print(op)
        print(cmd)
        print(cmd[0])
        print(cmd[0] == 'rect')
        raise Exception('parse error... expected "rotate" or "rect"')
    return X


def _initialGrid(shape):
    return np.zeros(shape)


def _main(data):
    display = _initialGrid(shape=(6, 50))
    for d in data:
        display = updateDisplay(display, d)
    return display


if __name__ == "__main__":
    data = load_data('./input/day8input.csv')
    display = _main(data)
    display_text = [['#' if x[j] == 1 else '.'
                     for j in range(len(x))]
                    for x in display.tolist()]
    for j in display_text:
        print(j)
    print('number of lit pixels:')
    print(display.sum())
