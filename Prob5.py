class LabelGenerator:
    def __init__(self, prefix, index=1):
        self._prefix = prefix
        self._index = index

    def next_label(self):
        output = f"{self._prefix}{self._index}"
        self._index += 1
        return output


if __name__ == "__main__":
    lg = LabelGenerator("Figure ")
    for _ in range(5):
        print(lg.next_label())

    lg = LabelGenerator("P", 0)
    for _ in range(5):
        print(lg.next_label())
