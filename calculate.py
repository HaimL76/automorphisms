class Scalar:
    def __init__(self, ui0: int, uj0: int, li0: int, lj0: int):
        self.ui = ui0
        self.uj = uj0
        self.li = li0
        self.lj = lj0

    def print(self, end=", "):
        print(f'a_(({self.ui},{self.uj}),({self.li},{self.lj}))', end=end)


class Element:
    def __init__(self, n0: int, i0: int, j0: int):
        self.n = n0
        self.i = i0
        self.j = j0
        self.scalars = []

        for l in range(1, self.n):
            for k in range(l+1, self.n+1):
                self.scalars.append(Scalar(self.i, self.j, l, k))

    def print(self):
        for scalar in self.scalars:
            scalar.print()


class Group:
    def __init__(self, n: int):
        self.elements = []

        for i in range(1, n):
            for j in range(i+1, n+1):
                self.elements.append(Element(n, i, j))

    def multiply_all(self):
        for element1 in self.elements:
            for element2 in self.elements:
                self.multiply(element1=element1, element2=element2)

    def multiply(self, element1: Element, element2: Element):
        relations: list = []

        for scalar1 in element1.scalars:
            for scalar2 in element2.scalars:
                li: int = 0
                lj: int = 0

                if scalar1.lj == scalar2.li:
                    li = scalar2.li
                    lj = scalar1.lj

                if scalar1.li == scalar2.lj:
                    li = scalar1.li
                    lj = scalar2.lj

                if li > 0 and lj > 0:
                    element: Element = None
                    index: int = 0

                    while element is None and index < len(self.elements):
                        element0: Element = self.elements[index]
                        index += 1

                        if element0.i == li and element0.j == lj:
                            element = element0

    def print(self):
        for element in self.elements:
            element.print()
            print()



