# Important extensions
import time
import random
import sys
import subprocess
import platform
import datetime
import os

 # Rich [For color and formatting]
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.spinner import Spinner
# from rich.table import Table
from rich.progress import Progress
# from rich.syntax import Syntax


import colorama
from colorama import Style, Fore

def checkForFunctionsAndCompileThem(returnCode, mainClassDeclaredByClient, codeToBeCompiled):
  countForAllCode = len(codeToBeCompiled)
  countForTrueCode = countForAllCode - 5
  
  for i in range(countForTrueCode):
    openBracket = "("
    closeBracket = ")"
    doubleQuotes = '"'
    try:
      currentFunctionInFocus = codeToBeCompiled[i+4]
      currentFunctionInFocus = currentFunctionInFocus.split("(")
      partOneOfFunction = currentFunctionInFocus[0]
      partTwoOfFunction = currentFunctionInFocus[1]
      if openBracket in currentFunctionInFocus[1]:
        if closeBracket in currentFunctionInFocus[1]:
          garbageCollector = ""
        
      elif closeBracket in currentFunctionInFocus[1]:
        garbageCollector = ""
    except IndexError:
      print(Fore.RED + f'ParenthesisAndQuoteIndexationOrAbsenceError' + Fore.RESET)
    consoleOutputArg = "console.output"
    consoleOutputColorArg = "console.output.color"
    consoleSleepArg = "console.sleep"
    consoleExit = "console.exit"

    
    if partOneOfFunction == consoleOutputArg:
      try:
        outpputStringVar = partTwoOfFunction.split('"')
        partTwoOfFunctionchars = [char for char in partTwoOfFunction]
        if partTwoOfFunctionchars[-1] == closeBracket:
          trashVariableFor0Output = ""
        else:
          print(Fore.RED + f'BracketPlacementOrAbsenceError: expected "{closeBracket}".' + Fore.RESET)
        if partTwoOfFunction[0] == doubleQuotes:
          trashVariableFor0Output = ""
        else:
          print(Fore.RED + f'QuotePlacementOrAbsenceError: expected `{doubleQuotes}`.' + Fore.RESET) 
        if partTwoOfFunctionchars[-2] == doubleQuotes:
            trashVariableFor0Output = ""
        else:
          print(Fore.RED + f'QuotePlacementOrAbsenceError: expected `{doubleQuotes}`.' + Fore.RESET)
      except IndexError:
        print(Fore.RED + f'QuotePlacementOrAbsenceError: expected `{doubleQuotes}`.' + Fore.RESET)
      outputString = outpputStringVar[1]
      print(Fore.RESET + outputString)
      
    elif partOneOfFunction == consoleOutputColorArg:
      commaBraking = partTwoOfFunction.split(",")
      partTwoOfFunction = partTwoOfFunction.split()
      if partTwoOfFunction[-1] == closeBracket:
        trashVariableFor0Output = ""
      else:
        print(Fore.RED + f'BracketPlacementOrAbsenceError: expected "{closeBracket}".' + Fore.RESET)
      if partTwoOfFunction[0] == doubleQuotes:
        trashVariableFor0Output = ""
      else:
        print(Fore.RED + f'QuotePlacementOrAbsenceError: expected `{doubleQuotes}`.' + Fore.RESET) 
      if partTwoOfFunction[-2] == doubleQuotes:
          trashVariableFor0Output = ""
      else:
        print(Fore.RED + f'QuotePlacementOrAbsenceError: expected `{doubleQuotes}`.' + Fore.RESET)
        
    elif partOneOfFunction == consoleSleepArg:
      print()
    elif partOneOfFunction == consoleExit:
      print(returnCode)
      quit()
    else:
      print(Fore.RED + f'FunctionDefineError: No function called "{currentFunctionInFocus}".' + Fore.RESET)
  


def compileOblFileToPython(codeToBeCompiled):
  codeBitsToCompile = codeToBeCompiled.split()
  
  # venv declaration!
  declaringVirtualEnvironment = 'venv'
  if codeBitsToCompile[0] == declaringVirtualEnvironment:
    print(Fore.MAGENTA + f'Declared {declaringVirtualEnvironment} for ' + Fore.WHITE + '.obl' + Fore.MAGENTA + ' program Dependencies.' + Fore.RESET)
  else: 
    print(Fore.RED + f'VirtualEnvironmentInitializationError: "venv" class not declared.' + Fore.RESET)
    quit()

  # {} formating
  numberOfOpenCurlyBracketsPlusOne = codeToBeCompiled.split('{')
  actualNumberOfOpenCurlyBracketsPlusOne = len(numberOfOpenCurlyBracketsPlusOne)
  actualNumberOfOpenCurlyBrackets = actualNumberOfOpenCurlyBracketsPlusOne - 1
  
  numberOfClosedCurlyBracketsPlusOne = codeToBeCompiled.split('}')
  actualNumberOfClosedCurlyBracketsPlusOne = len(numberOfClosedCurlyBracketsPlusOne)
  actualNumberOfClosedCurlyBrackets = actualNumberOfClosedCurlyBracketsPlusOne - 1
  
  if actualNumberOfOpenCurlyBrackets == actualNumberOfClosedCurlyBrackets:
    print('Formatted "{}" Syntax Requirement')
  elif actualNumberOfOpenCurlyBrackets > actualNumberOfClosedCurlyBrackets:
    print(Fore.RED + 'ParenthesisFormatingError: invalid syntax, expected a "}"' + Fore.RESET)
    quit()
  elif actualNumberOfOpenCurlyBrackets < actualNumberOfClosedCurlyBrackets:
    print(Fore.RED + 'ParenthesisFormatingError: invalid syntax, expected a "{"' + Fore.RESET)
    quit()
  else:
    print(Fore.RED + 'ParenthesisFormatingError: invalid syntax for "{}"' + Fore.RESET)
    
    
  #Checking for Parathesis Placement
  openCurlyBrackets = "{"
  if codeBitsToCompile[1] == openCurlyBrackets:
    print("Compiling " + Fore.MAGENTA + "venv{}" + Fore.RESET)
  else:
    (Fore.RED + 'ParenthesisPlacementError: invalid syntax, expected a "{"' + Fore.RESET)
    
  closeCurlyBrackets = "}"
  if codeBitsToCompile[-1] == closeCurlyBrackets:
    print("venv.close{}")
  else:
    (Fore.RED + 'ParenthesisPlacementError: invalid syntax, expected a "}"' + Fore.RESET)

  mainConsole = "main.console()"
  mainVoid = "main.void()"
  mainVoidBits = mainVoid.split("(")
  mainConsoleBits = mainConsole.split("(")
  consoleMainHogger = codeBitsToCompile[2]
  consoleMainHoggerBits = consoleMainHogger.split("(")
  if consoleMainHoggerBits[0] == mainConsoleBits[0]:
    print(Fore.GREEN + f'Initializing Main.console [consoleMainHoggerBits]' + Fore.RESET)
    hoggerBitsFromMain = consoleMainHoggerBits[1]
    typeOfMainClass = 'console'
  elif consoleMainHoggerBits[0] == mainVoidBits[0]:
    print(Fore.GREEN + f'Initializing Main.void [voidMainHoggerBits]' + Fore.RESET)
    hoggerBitsFromMain = consoleMainHoggerBits[1]
    typeOfMainClass = 'void'
  else:
    print(Fore.RED + 'MainClassCallError: invalid call for Main Class"' + Fore.RESET)
    quit()
    
    
    
  hoggerBitsFromMainChar = [char for char in hoggerBitsFromMain]
  closeBracketsForMainClass = ")"
  if hoggerBitsFromMain[-1] == closeBracketsForMainClass:
    trashVariableFor0Output = "" # Loading Bar
    with Progress(transient=True) as progress:
      taskOneAsCompilingOblFile = progress.add_task("[cyan]CompilingOblFile...", total=170)
      taskTwoAsCheckingForSyntaxError = progress.add_task("[magenta]CheckingForSyntaxError", total=200)
      taskThreeAsProcessingIndents = progress.add_task("[yellow]ProcessingIndentsAndBugs", total=180)
      
      
      while not progress.finished:
        progress.update(taskOneAsCompilingOblFile, advance=random.randint(1, 10))
        progress.update(taskTwoAsCheckingForSyntaxError, advance=random.randint(1, 10))
        progress.update(taskThreeAsProcessingIndents, advance=random.randint(1, 10))
        time.sleep(random.uniform(0.1, 0.3))
  else:
    print(Fore.RED + 'MainCloseBracketSyntaxError: absence of ")" from Main Class declaration.' + Fore.RESET)
    
    
  returnCodeAfterSuccess = ""
  for i in range(len(hoggerBitsFromMainChar) - 1):
    returnCodeAfterSuccess = returnCodeAfterSuccess + hoggerBitsFromMainChar[i]
  #print(returnCodeAfterSuccess)
  
  if codeBitsToCompile[3] == openCurlyBrackets:
    trashVariableFor0Output = "" #Loading
    console = Console()
    with console.status("[bold magenta]ExtractingCodeFromOblFile...") as status:
          time.sleep(4)
  else:
    print(Fore.RED + 'MainOpenCurlyBracketSyntaxError: absence of "{" from Main Class declaration.' + Fore.RESET)
  if codeBitsToCompile[-2] == closeCurlyBrackets:
    trashVariableFor0Output = ""
  else:
    print(Fore.RED + 'MainCloseCurlyBracketSyntaxError: absence of "}" from Main Class declaration.' + Fore.RESET)
  checkForFunctionsAndCompileThem(returnCodeAfterSuccess, typeOfMainClass, codeBitsToCompile)
  
  
  
requestByClient = input(Fore.GREEN + '$ ')
print(Fore.RESET)
requestByClient = requestByClient.split()

# commandValues
compileRequestByClient = 'obl.compile'

if requestByClient[0] == compileRequestByClient:
  nameOfFileToBeCompiled = requestByClient[1]
  with open(nameOfFileToBeCompiled, 'r') as file:
    codeExtractedFromClientOblFile = file.read()
    file.close()
  compileOblFileToPython(codeExtractedFromClientOblFile)
else:
  print(Fore.RED + f'ERROR: "{requestByClient[0]}" is not a valid Request' + Fore.RESET)