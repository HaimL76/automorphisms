class Scalar:
    def __init__(self, ui0: int, uj0: int, li0: int, lj0: int):
        self.ui = ui0
        self.uj = uj0
        self.li = li0
        self.lj = lj0

    def print(self, end=", "):
        print(f'a_(({self.ui},{self.uj}),({self.li},{self.lj}))', end=end)


class Element:
    def __init__(self, n0: int, ui0: int, uj0: int):
        self.n = n0
        self.ui = ui0
        self.uj = uj0
        self.scalars = []

        for i in range(1, self.n):
            for j in range(i+1, self.n+1):
                self.scalars.append(Scalar(ui0, uj0, i, j))

    def print(self):
        for scalar in self.scalars:
            scalar.print()


class Group:
    def __init__(self, n: int):
        self.elements = []

        for i in range(1, n):
            for j in range(i+1, n+1):
                self.elements.append(Element(n, i, j))

    def print(self):
        for element in self.elements:
            element.print()
            print()



