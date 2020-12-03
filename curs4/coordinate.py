class Coordinate(object):
    """ O coordonata este compuna din valorile x si y """

    def __init__(self, x, y):
        """ Setam valorile pentru x si y"""
        self.x = x
        self.y = y

    def __str__(self):
        """Afisam coordonatele x si y"""
        return f'<{self.x}, {self.y}>'

    def __add__(self, other):
        """Adunare a doua coordonate"""
        self.x += other.x
        self.y += other.y

    def __sub__(self, other):
        """Scaderea a doua coordonate"""
        self.x -= other.x
        self.y -= other.y

    def __eq__(self, other):
        """Egalitatea a doua coordonate"""
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def distance(self, other):
        """Returneaza distanta euclidiana dinre 2 coordonate"""
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5


origin = Coordinate(0, 0)
print(id(origin))
print(origin)

c1 = Coordinate(1, 0)
c2 = Coordinate(0, 2)
print(c1, c2)

print(origin.distance(origin))
print(c1.distance(origin))
print(c2.distance(origin))
print(c1.distance(c2))

if origin == c1:
    print('Sunt egale')
else:
    print('Nu sunt egale')
