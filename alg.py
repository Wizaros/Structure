class Lama:
    def __init__(self):
        self.symbols = []
        self.digits = []
        self.others = []

    def add(self, s: str):
        for char in s:
            if char.isdigit():
                self.digits.append(char)
            elif char.isalpha():
                self.symbols.append(char)
            else:
                self.others.append(char)

    def clear(self):
        self.symbols.clear()
        self.digits.clear()
        self.others.clear()

    def pop_symbol(self):
        if self.symbols:
            return self.symbols.pop(-1)
        else:
            return None

    def pop_digit(self):
        if self.digits:
            return self.digits.pop(-1)  
        else:
            return None

    def pop_other(self):
        if self.others:
            return self.others.pop(-1)  
        else:
            return None

data = Lama()
string = input("Введите строку: ")
data.add(string)
symbol = data.pop_symbol()
digit = data.pop_digit()
other = data.pop_other()
print("Буквы:", data.symbols, "| Цифры:", data.digits, "| Символы:", data.others)
print("Удаленные элементы: ", symbol, digit, other) 