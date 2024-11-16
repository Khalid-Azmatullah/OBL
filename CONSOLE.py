from COMMONS.CheckKeyword import CheckKeyword


class Console:

  def __init__(self):
    self.console = True

  def Output(self, Line):
    return CheckKeyword('OUTPUT', Line)

  def Input(self, Line):
    return CheckKeyword('INPUT', Line)
