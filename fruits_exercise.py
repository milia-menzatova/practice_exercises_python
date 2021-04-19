class Fruit():
    def __init__(self):
        print("Hello my fruit")
    def nutrition(self):
        print("My fruit has super nutrition")
    def fruit_shape(self):
        print("You need fruits")

class Lemon(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        print("Hello People, I'm super delicious fruit Lemon")
    def nutrition(self):
        print("So yummy")
    def color(self):
        print("My color is yellow")

f = Fruit()
f.nutrition()
f.fruit_shape()

l = Lemon()
l.fruit_shape()
l.nutrition()
l.color()
