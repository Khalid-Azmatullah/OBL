class console:

  def __init__(self):
    self.version = "0.0.1"

  def log(self, Line):
    print(Line)

  def error(self, Line):
    print(f'Error: {Line}')
    quit()

  def warn(self, Line):
    print(f'Warning: {Line}')

