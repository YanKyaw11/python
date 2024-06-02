class Bird:
    name = "crow"
    size = 10
    color = "black"
    food = "rice"

    def eat(self):
        print(self.name, "is eating ",self.food)

crow = Bird()
crow.eat()

eagle = Bird()
eagle.eat()