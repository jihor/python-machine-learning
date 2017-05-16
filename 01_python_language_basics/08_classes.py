class Person:
    name = 'Smith'

    # self is mandatory for instance methods
    def set_name(self, v):
        print("Setting name to {}".format(v))
        self.name = v

    def __init__(self, name):
        print("This is object initializer")
        self.set_name(name)

me = Person('Jihor')
print("I am", me.name)
