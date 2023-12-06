def mystery(x, y=10):
    z = len(x)
    return puzzle(x, y) + puzzle(w[: enigma(z, 3)], y)


def enigma(x, w):
    return x - w**2


def puzzle(y, z):
    return y[z:]


w = "gingerbread man"
print(mystery(w, -3))
