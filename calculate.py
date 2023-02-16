class Scalar:
    def __init__(self, ui0: int, uj0: int, li0: int, lj0: int):
        self.ui = ui0
        self.uj = uj0
        self.li = li0
        self.lj = lj0

    def __str__(self):
        return f'a_(({self.ui},{self.uj}),({self.li},{self.lj}))'


class Product(object):
    def __init__(self, left0: Scalar, right0: Scalar, is_plus0: bool):
        self.left = left0
        self.right = right0
        self.is_plus = is_plus0


class Element(object):
    def __init__(self, n0: int, i0: int, j0: int):
        self.n = n0
        self.i = i0
        self.j = j0
        self.scalars = []
        self.products = []

        for l in range(1, self.n):
            for k in range(l + 1, self.n + 1):
                self.scalars.append(Scalar(self.i, self.j, l, k))

    def __str__(self):
        str0: str = ""

        for index0 in range(len(self.scalars)):
            scalar: Scalar = self.scalars[index0]

            if index0 > 0:
                str0 += ", "

            str0 += str(scalar)

        return str0


def multiply(element1: Element, element2: Element) -> Product:
    products: list = []

    for scalar1 in element1.scalars:
        for scalar2 in element2.scalars:
            li: int = 0
            lj: int = 0

            is_plus: bool = False

            if scalar1.lj == scalar2.li:
                li = scalar1.li
                lj = scalar2.lj

                is_plus = True

            if scalar1.li == scalar2.lj:
                li = scalar2.li
                lj = scalar1.lj

                is_plus = False

            if li > 0 and lj > 0:
                products.append(Product(scalar1, scalar2, is_plus))

    return products


class Group(object):
    def __init__(self, n: int):
        self.elements = []

        for i in range(1, n):
            for j in range(i + 1, n + 1):
                self.elements.append(Element(n, i, j))

    def multiply_all(self):
        for element1 in self.elements:
            for element2 in self.elements:
                element: Element = self.get_product_element(element1, element2)

                products: list = multiply(element1, element2)

                if element is not None:
                    for product in products:
                        if isinstance(product, Product):
                            element.products.append(product)

    def get_product_element(self, element1: Element, element2: Element):
        element: Element = None

        i1: int = element1.i
        j1: int = element1.j

        i2: int = element2.i
        j2: int = element2.j

        i: int = 0
        j: int = 0

        if j1 == i2:
            i = i1
            j = j2

        if i1 == j2:
            i = i2
            j = j1

        if i > 0 and j > 0:
            index0: int = 0

            while element is None and index0 < len(self.elements):
                element0: Element = self.elements[index0]
                index0 += 1

                if element0.i == i and element0.j == j:
                    element = element0

        return element

    def print(self):
        for element in self.elements:
            print(element, end="")
            print()

        for element in self.elements:
            for product in element.products:
                left = product.left
                right = product.right

                plus_minus = '+'

                if not product.is_plus:
                    plus_minus = '-'

                if left is not None and right is not None:
                    print(f'{plus_minus} {left} * {right}', end="")

            print()
