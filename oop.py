class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("bark")

    # def meow(self):
    #     print("meow")
    
    # def addOne(self, x):
    #     print(x + 1)

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age
        print(self.name , "is now" , self.age , ".")

# d = Dog("Doggy", 1012391)
# print(d.name)
# print(d.get_age(), d.get_name())

# d2 = Dog("Cat", 2)
# print(d2.name)
# print(d2.get_age(), d2.get_name())

# d2.set_age(5)

# d.meow()
# d.bark()
# # d.addOne(5)

# print(type(d))

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

# s1 = Student("Wayne", 15, 93)
# s2 = Student("Tim", 19, 95)
# s3 = Student("Bob", 17, 73) 

# course = Course("Science", 2)
# course.add_student(s1)
# course.add_student(s2)
# print(course.add_student(s3))
# print(course.get_average_grade())

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print("I can't speak :P")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow!")

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old, and I am {self.color}.")

class Dog(Pet):
    def speak(self):
        print("Bark!")

class Fish(Pet):
    pass

# t = Pet("Tim", 19)
# t.show()
# b = Cat("Bill", 123)
# b.show()
# d = Dog("Doug", 3)
# d.speak()
# f = Fish("Vandal", 1)
# f.speak()


class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        # Person.number_of_people += 1
        Person.add_person()
    
    @classmethod
    def number_of_peoples(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

# p1 = Person("Tim")
# p2 = Person("Sim")

# print(Person.number_of_people)

# Person.number_of_people = 2
# print(p1.number_of_people)
# print(p2.number_of_people)

# print(Person.number_of_peoples())

class Math:

    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10
    
    @staticmethod
    def pr():
        print("run")

print(Math.add5(5))