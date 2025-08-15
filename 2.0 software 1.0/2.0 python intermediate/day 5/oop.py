# Object Oriented Programming
# taking real-life objects and trying to model them in your code
# constructor is needed after creating your class has 3 objects (self) that are created empty initially
# and stuff can be added in it in the future the xtis can be added but are done manually

class Student:
    def __init__(self, name, matricule, gpa, gender):     # this constructor creates an object by default called "self" you can add the properties(variables inside a class) of that objects
        # but they've just been added and it just creates space for them. You then go below to initalize them manually
        """Initailizing properties of this class"""
        # properties (attributes)
        self.name=name      # using "self." to get into the  object called self
        self.matricule=matricule
        self.gpa=gpa
        self.gender=gender
        # pass
        
        # Methods
    def take_lesson(self):              # a function inside a class is called a method hence this is a method
        return f"{self.name}, gender: {self.gender} with matricule {self.matricule} has registred a course"
    def drop_lesson(self):
         return f"{self.name}, gender: {self.gender} with matricule {self.matricule} has dropped a course"
    def resit_lesson(self):
         return f"{self.name}, gender: {self.gender} with matricule {self.matricule} has registered for a resit course"
    def get_result(self):
          return f"{self.name}, gender: {self.gender} with matricule {self.matricule} has result: {self.gpa}"
    def skip_class(self):
        return f"{self.name}, gender: {self.gender} with matricule {self.matricule} has skipped a class"
        
# creating instances (objects) of this class
first_student=Student("Allen", "Uba23E02", 3.9, "Male")
second_student=Student("Mbom", "Uba203ed", 1.1, "other")
print(f"First student is: {first_student.take_lesson()}")       #  print(f"First student is: {first_student}") this would just access the location in that space not the name properly
print(f"First student is: {first_student.drop_lesson()}")   
print(f"First student is: {first_student.resit_lesson()}")   
print(f"First student is: {first_student.get_result()}")
print(f"First student is: {first_student.skip_class()}")
   