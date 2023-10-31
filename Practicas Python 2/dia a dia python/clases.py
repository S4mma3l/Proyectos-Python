class MyEmptyPerson:
    pass


print(MyEmptyPerson)


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def walk(self):
        print(f"{self.name}{self.surname} esta estudiando")


my_person = Person("Angel", "Hernandez")
print(f"{my_person.name} {my_person.surname}")
my_person.walk()
