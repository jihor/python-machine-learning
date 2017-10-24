class Person:

    # the doc, if present, has to be the first thing in code block
    """
    class Person

    This is the documentation for Person class.
    It can be accessed using special __doc__ field
    """
    # alternatively __doc__ = "..." can be used

    __author__ = "jihor (jihor@yandex.ru)"
    __copyright__ = "Copyright 2017, ACME Corp."

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


print(Person.__doc__)
print(Person.__author__)
print(Person.__copyright__)
