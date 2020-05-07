class vector:
    'doc str'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return vector(self.x + other.x, self.y + other.y)

    def substruct(self, other):
        return vector(self.x * other.x, self.y * other.y)

    def multiply(self, number):
        return vector(self.x * number, self.y * number)

    def show(self):
        print(self.x, self.y)
