class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return f"{self.real}+{self.imag}j" if self.imag >= 0 else f"{self.real}{self.imag}j"

    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real
        )

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        if denominator == 0:
            raise ValueError("Деление на ноль невозможно.")
        return Complex(
            (self.real * other.real + self.imag * other.imag) / denominator,
            (self.imag * other.real - self.real * other.imag) / denominator
        )

    def __abs__(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5


# Пример использования
try:
    c1 = Complex(
        float(input("Введите действительную часть первого комплексного числа: ")),
        float(input("Введите мнимую часть первого комплексного числа: "))
    )
    c2 = Complex(
        float(input("Введите действительную часть второго комплексного числа: ")),
        float(input("Введите мнимую часть второго комплексного числа: "))
    )
    c3 = int(input("сумма - 1, разность - 2, произведение - 3, частное - 4, модуль первого - 5: "))

    if c3 < 1 or c3 > 5:
        print("Ошибка: недопустимый выбор операции.")
    else:
        if c3 == 1:
            print("Сумма комплексных чисел:")
            print(c1 + c2)
        elif c3 == 2:
            print("Разность комплексных чисел:")
            print(c1 - c2)
        elif c3 == 3:
            print("Произведение комплексных чисел:")
            print(c1 * c2)
        elif c3 == 4:
            print("Частное комплексных чисел:")
            print(c1 / c2)
        elif c3 == 5:
            print("Модуль первого комплексного числа:")
            print(abs(c1))
except ValueError as ve:
    print(f"Ошибка ввода: {ve}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
