# 3 attributes and 3 methods for each class

# - Student:
#   - Attributes: Name (str), Grades (list), Year (int)
#   - Methods: GoToClass, DoHomework, TakeTest

# - Teacher:
#   - Attributes: Name (str), Is Friendly (bool), Good Instructor (bool)
#   - Methods: GiveHomework, GiveTests, GradeWork (both tests and homework)

# - Course:
#   - Attributes: Course Name (str), Honors/AP (bool), A-G Requirement (bool) --> Means elective or non/elective
#   - Methods: ApplyStudentGrade, AddCourse, DropCourse


class Student():
  def __init__(self, name, year = 1):  # Default freshman if school year isn't supplied
    self.name = name
    self.year = year
    self.reportCard = {}  # SYNTAX: {Class Name: Class Grade (A-F, NO NUMBERS, +, OR -)}

  def __repr__(self):

    match self.year:
      case 1: 
        return f"Welcome to high school, {self.name}! This is your first year in high school, so you're a freshman, enjoy your time!" 
      
      case 2:
        return f"Welcome back, {self.name}! We hope you enjoyed your freshman year, and we hope you enjoy your new sophomore year even more."
      
      case 3:
        return f"{self.name}{self.name[-1] * 3}, good to see you again! You're heading into your junior year, which means you're half way done with high school. Hang in there!"
      
      case 4:
        return f"Alright, let's do this one last time. You're {self.name}, and you're a senior in high school. Catch onto that Spider-Man: ITSV reference?"
      
      case _:
        return "You're not supposed to be in high school... you're too old."
    
  

class Teacher():
  def __init__(self, name, is_friendly = True, good_instructor = True):
    self.name = name
    self.friendly = is_friendly
    self.good_instructor = good_instructor

  def __repr__(self):
    return f"Hello, {self.name}. Welcome to your class!"


class Course():
  def __init__(self, name, advanced = False, ge = True):  # Default non-Honors/AP class and default A-G required class
    self.courseName = name
    self.advancedClass = advanced
    self.genEd = ge

  def __repr__(self):
    message = f"You chose the {self.courseName} class. "

    match self.advancedClass:
      case True:
        
        match self.genEd:
          case True:
            message += f"This is an advanced course, and it fulfills one of your A-G requirements."
          
          case False:
            message += f"This is an advanced course, and it does not fulfill one of your A-G requirements."
      
      case False:
        
        match self.genEd:
          case True:
            message += f"This is not an advanced course, and it fulfills one of your A-G requirements."
          
          case False:
            message += f"This is not advanced course, and it does not fulfill one of your A-G requirements."

    return message
  
