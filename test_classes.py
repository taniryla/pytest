class Person:
    def __init__(self, name):
        self.name = name

def test_classes_compare():
    p1 = Person("Mindy")
    p2 = Person("Daniel")
    assert p1.name == p2.namess