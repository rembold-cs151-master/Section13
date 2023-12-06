class Frosty:
    def __init__(self, n, c):
        self.wild = [c]
        self.n = n

    def snowball(self, h=3):
        self.n -= h
        self.wild += [self.n]

    def cap(self):
        return self.wild


f = Frosty(8, 15)
f.snowball()
f.snowball(1)
A = f.cap()
A.append(1)
print(sum(f.cap()))
