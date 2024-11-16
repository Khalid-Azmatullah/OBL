from JavaScript.JavaScript import console
from CHECK import Check
from CONSOLE import Console
from COMMONS.clearCache import clearCache

console = console()
Check = Check()
Console = Console()

FileName = 'main.obl'

with open(FileName, 'r') as File:
  Data = File.read()

ParsedData = Data.splitlines()

# INCLUDE CHECK
IncludedImports = []
for LineCount in range(len(ParsedData)):
  Line = ParsedData[LineCount]
  Line = Line.split(' ')
  if Check.Include(Line[0].strip()):
    if Check.Console(Line[1].strip()):
      IncludedImports.append('CONSOLE')
    elif Check.Var(Line[1].strip()):
      IncludedImports.append('VAR')
    else:
      console.error(f'NO VALID MODULE \'{Line[1].strip()}\' FOUND')
  elif Check.Main(Line[0].strip()):
    break

# CONSOLE RUN
for LineCount in range(len(ParsedData)):
  Line = ParsedData[LineCount]
  Line = Line.split(' ')
  if Check.Console(Line[0].strip()):
    if Console.Output(Line[1].strip()):
      print(Line)


clearCache()