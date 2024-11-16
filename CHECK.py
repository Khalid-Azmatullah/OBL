from COMMONS.CheckKeyword import CheckKeyword

class Check:

  def __init__(self):
    self.check = True

  def Include(self, Line):
    return CheckKeyword('INCLUDE', Line)

  def Console(self, Line):
    return CheckKeyword('CONSOLE', Line)

  def Var(self, Line):
    return CheckKeyword('VAR', Line)

  def Main(self, Line):
    return CheckKeyword('MAIN', Line)
