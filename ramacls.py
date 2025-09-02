class Student:
    school = "NPS School"
    school_id = 101

    def __init__(self, id, name):
        self.name = name
        self.id = id

    def show(self):  # Instance method
        return f"{self.name} studies in {self.school} and id is {self.school_id}"

    @classmethod
    def change_school(cls, new_name, new_id):  # Class method
        cls.school = new_name
        cls.school_id = new_id

    @staticmethod
    def info():  # Static method
        return "This is the Student class with std details and schl details."

# Usage
s1 = Student(101,"karthik")
print(s1.show())               # Instance method → needs object
Student.change_school("XYZ",102)   # Class method → modifies class variable
print(s1.show())
       
        # Now school is "XYZ"
print(Student.info())          # Static method → general info
