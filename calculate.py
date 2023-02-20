class Scalar:
    def __init__(self, ui0: int, uj0: int, li0: int, lj0: int):
        self.ui = ui0
        self.uj = uj0
        self.li = li0
        self.lj = lj0
        self.is_zero = False
        self.products = []

    def __str__(self):
        if self.is_zero:
            return "0"
        else:
            if isinstance(self.products, list) and len(self.products):
                str0: str = ''

                for product in self.products:
                    if isinstance(product, Product):
                        str0 += str(product)

                return str0
            else:
                return f'a_(({self.ui},{self.uj}),({self.li},{self.lj}))'


class Product(object):
    def __init__(self, i0: int, j0: int, left0: Scalar, right0: Scalar, is_plus0: bool):
        self.i = i0
        self.j = j0
        self.left = left0
        self.right = right0
        self.is_plus = is_plus0

    def __str__(self):
        plus_minus: str = '-'

        if self.is_plus:
            plus_minus = '+'

        return f'{plus_minus}{self.left}*{self.right}'


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

    def compare_scalars(self):
        zeros: list = []

        if isinstance(self.scalars, list) and len(self.scalars) > 0:
            for scalar in self.scalars:
                if isinstance(scalar, Scalar):
                    li: int = scalar.li
                    lj: int = scalar.lj

                    prods: list = []

                    if isinstance(self.products, list) and len(self.products) > 0:
                        for product in self.products:
                            if isinstance(product, Product):
                                if li == product.i and lj == product.j:
                                    prods.append(product)

                    if len(prods) > 0:
                        for prod in prods:
                            scalar.products.append(prod)
                    else:
                        scalar.is_zero = True




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
                products.append(Product(li, lj, scalar1, scalar2, is_plus))

    return products


class Group(object):
    def __init__(self, n: int):
        self.equal_to_zero = []
        self.elements = []

        for i in range(1, n):
            for j in range(i + 1, n + 1):
                self.elements.append(Element(n, i, j))

    def multiply_all(self):
        for element1 in self.elements:
            for element2 in self.elements:
                i1: int = element1.i
                j1: int = element1.j

                i2: int = element2.i
                j2: int = element2.j

                if i1 < j2 and (i1 < i2 or j1 < j2):
                    element: Element = self.get_product_element(element1, element2)

                    products: list = multiply(element1, element2)

                    if element is not None:
                        for product in products:
                            if isinstance(product, Product):
                                element.products.append(product)
                    else:
                        self.equal_to_zero.append((element1, element2, products))

        for element in self.elements:
            if isinstance(element, Element) and element.j > element.i + 1:
                element.compare_scalars()

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
            print(f'E_({element.i},{element.j})=', end="")

            for product in element.products:
                left = product.left
                right = product.right

                plus_minus = '+'

                if not product.is_plus:
                    plus_minus = '-'

                if left is not None and right is not None:
                    print(f'{plus_minus} {left} * {right}', end="")

            print()

        for tup in self.equal_to_zero:
            element1: Element = tup[0]
            element2: Element = tup[1]

            print(f'E_({element1.i},{element1.j})*E_({element2.i},{element2.j})=', end="")

            for product in tup[2]:
                left = product.left
                right = product.right

                plus_minus = '+'

                if not product.is_plus:
                    plus_minus = '-'

                if left is not None and right is not None:
                    print(f'{plus_minus} {left} * {right}', end="")

            print()
