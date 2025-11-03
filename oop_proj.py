class School():
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def get_name(self):
    return self.name

  def get_level(self):
    return self.level
  
  def get_numberOfStudents(self):
    return self.numberOfStudents

  def set_numberOfStudents(self, number):
    self.numberOfStudents = number

  def __repr__(self):
    return f'A {self.level} school named {self.name} with {self.numberOfStudents} students'

class PrimarySchool(School):

  def __init__(self, name, numberOfStudents, pickupPolicy):

    self.pickupPolicy = pickupPolicy

    super().__init__(name, 'primary', numberOfStudents)

  def get_pickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + f'The pickup policy is {self.pickupPolicy}'

class HighSchool(School):
  def __init__(self, name, numberOfStudents, Sports):

    # self.Sports = Sports

    super().__init__(name, 'High School', numberOfStudents)
    self.Sports = Sports
  
  def get_Sports(self):
    return self.Sports

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + f'the sports teams include {self.Sports}'

school = School('UMD', 'uni', 10000)
print(school)
print(school.get_name())
print(school.get_level())
school.set_numberOfStudents(12000)
print(school.get_numberOfStudents())

ps = PrimarySchool('elm', '500', 'pickup after 2')
print(ps)

hs = HighSchool('High', '1000', '[basketball, football, volleyball, tennis]')
print(hs)
