# Going to create a high-school simulator
# Classes will include: Student, Teacher, Courses

# 3 attributes and 3 methods for each class

# - Student:
#   - Attributes: Name (str), Grades (list), Year (int)
#   - Methods: GoToClass, DoHomework, TakeTest

# - Teacher:
#   - Attributes: Name (str), Is Friendly (bool), Good Instructor (bool)
#   - Methods: GiveHomework, GiveTests, GradeWork (both tests and homework)

# - Courses:
#   - Attributes: Course Name (str), Honors/AP (bool), A-G Requirement (bool) --> Means elective or non/elective
#   - Methods: ApplyStudentGrade, AddCourse, DropCourse

class Student():
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return f"Hello, {self.name}. Welcome to high school!"

class Teacher():
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return f"Hello, {self.name}. Welcome to your class!"


class Courses():
  def __init__(self):
    pass
  

# Test instances

BRANDON = Student("Dzrk")
mrMercado = Teacher("Mr. Mercado")
schedule = Courses()

print(BRANDON)
print(mrMercado)