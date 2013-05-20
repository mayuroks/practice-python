class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * 3.1459

c = Circle(5)
c.radius = 3
print(c.area())

print(Circle.area(c))
