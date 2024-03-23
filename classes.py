class Person():
    def  __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def __str__(self):
        return f"{self.name} :: {self.gender}"

mireku = Person("mireku", "male")   
print(mireku)     