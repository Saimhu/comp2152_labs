
class Person:

    def __init__(self, name, age, height):
        print("Constructing the Person object")
        self.__name = name
        self.__age = age
        self.__height = height

        self.public_prop = "I'm public"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def __del__(self):
        print("The garbage collector is automatically destroying the Person object")


person1 = Person("Mark", 20, 6)

print("Public property:", person1.public_prop)


print("Name:", person1.name)

person1.name = "Anna"

print("Updated Name:", person1.name)