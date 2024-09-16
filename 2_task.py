import math


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def from_string(cls, s):
        x, y, z = map(float, s.split(','))
        return cls(x, y, z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __ne__(self, other):
        return not self.__eq__(other)
def farthest_point(points):
    max_length = 0
    farthest = None
    for point in points:
        if point.length() > max_length:
            max_length = point.length()
            farthest = point
    return farthest

# Пример использования
n = int(input())
points = [Vector.from_string(input()) for _ in range(n)]
farthest = farthest_point(points)
print(f"Точка, наиболее удаленная от начала координат: {farthest}")

def center_of_mass(points):
    if not points:
        return None
    n = len(points)
    sum_x = sum(point.x for point in points)
    sum_y = sum(point.y for point in points)
    sum_z = sum(point.z for point in points)
    return Vector(sum_x / n, sum_y / n, sum_z / n)

# Пример использования
center = center_of_mass(points)
print(f"Центр масс: {center}")

def cross_product(v1, v2):
    return Vector(
        v1.y * v2.z - v1.z * v2.y,
        v1.z * v2.x - v1.x * v2.z,
        v1.x * v2.y - v1.y * v2.x
    )

def parallelogram_area(v1, v2):
    cross_prod = cross_product(v1, v2)
    return cross_prod.length()

# Пример использования
v1 = Vector.from_string(input())
v2 = Vector.from_string(input())
print(f"Площадь параллелограмма: {parallelogram_area(v1, v2)}")

def scalar_triple_product(v1, v2, v3):
    cross_prod = cross_product(v2, v3)
    return v1 * cross_prod

def parallelepiped_volume(v1, v2, v3):
    return abs(scalar_triple_product(v1, v2, v3))

# Пример использования
v1 = Vector.from_string(input())
v2 = Vector.from_string(input())
v3 = Vector.from_string(input())
print(f"Объём параллелепипеда: {parallelepiped_volume(v1, v2, v3)}")

def distance(v1, v2):
    return math.sqrt((v1.x - v2.x)**2 + (v1.y - v2.y)**2 + (v1.z - v2.z)**2)

def perimeter(v1, v2, v3):
    return (distance(v1, v2) + distance(v2, v3) + distance(v3, v1))

def max_perimeter(points):
    max_perim = 0
    best_triangle = None
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                perim = perimeter(points[i], points[j], points[k])
                if perim > max_perim:
                    max_perim = perim
                    best_triangle = (points[i], points[j], points[k])
    return max_perim

# Пример использования
print(f"Максимальный периметр треугольника: {max_perimeter(points)}")

def triangle_area(v1, v2, v3):
    a = v2 - v1
    b = v3 - v1
    cross_prod = cross_product(a, b)
    return 0.5 * cross_prod.length()

def max_area(points):
    max_area = 0
    best_triangle = None
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                area = triangle_area(points[i], points[j], points[k])
                if area > max_area:
                    max_area = area
                    best_triangle = (points[i], points[j], points[k])
    return max_area

# Пример использования
print(f"Максимальная площадь треугольника: {max_area(points)}")
