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

# varibles for functions
open_curly_brackets = '{'                                         #
close_curly_brackets = '}'                                        #
open_brackets = '('                                               #
close_brackets = ')'                                              #
space = ' '                                                       #
null = ''                                                         #
double_quote = '"'                                                #
comment_hash = '#'                                                #
true = 'true'                                                     #
false = 'false'                                                   #


functions_list_with_no_dependencies_for_main = [
  'console.output', 
  'console.output.color', 
  'console.sleep', 
  'console.end'
]

def return_code(code_for_return):
  print(Fore.GREEN + code_for_return + Fore.RESET)
    


def main_commands_compiler(code_command_elements):
  num_of_commands = len(code_command_elements)
  
  console_output_variable_by_client = ''
  
  for i in range(num_of_commands):
    try:
      console_output_variable_by_client = ''
      current_command_to_be_compiled = code_command_elements[i]
      current_command_to_be_compiled_p1 = current_command_to_be_compiled.split(open_brackets, 1)
      current_command_to_be_compiled_p2 = current_command_to_be_compiled_p1[-1]
      current_command_to_be_compiled_p1 = current_command_to_be_compiled_p1[0]
    except IndexError:
      error('FunctionError: ', f'No valid function {double_quote}{code_command_elements[i]}{double_quote}')
    try:
      index = functions_list_with_no_dependencies_for_main.index(current_command_to_be_compiled_p1)
      garbage_collect()
    except ValueError:
      error('FunctionError: ', f'No valid function {double_quote}{current_command_to_be_compiled_p1}{double_quote}')
    
    if index == 0:
      if current_command_to_be_compiled_p2[-2] == close_brackets:
        if current_command_to_be_compiled_p2[0] == double_quote:
          if current_command_to_be_compiled_p2[-3] == double_quote:
            for i in range(len(current_command_to_be_compiled_p2) - 3):
              console_output_variable_by_client = console_output_variable_by_client + current_command_to_be_compiled_p2[i]
            console_output_variable_by_client = console_output_variable_by_client.lstrip('"')
            print(console_output_variable_by_client)
          else:
            error('QuotationErrorForString: ', f'did not use {double_quote} for ' + Fore.YELLOW +  f'{current_command_to_be_compiled_p2}' + Fore.RESET)
        else:
          error('QuotationErrorForString: ', f'did not use {double_quote} for ' + Fore.YELLOW +  f'{current_command_to_be_compiled_p2}' + Fore.RESET)
      else:
        error('BracketUsageError: ', f'did not use {double_quote}{close_brackets}{double_quote} for {double_quote}{current_command_to_be_compiled_p2}{double_quote}')
  
  
def garbage_collect():                                            #
  garbage_collector = ''                                          #

def error(error_name, message):
  print(Fore.RED + error_name + Fore.RESET + message )
  quit()

def run_basic_code_compiler():                                    #

  # check for curly brackets
  number_of_open_curly_brackets = len(code.split(open_curly_brackets)) - 1            #
  number_of_close_curly_brackets = len(code.split(close_curly_brackets)) - 1          #
  if number_of_open_curly_brackets == number_of_close_curly_brackets:
    garbage_collect()
  else:
    error('ParenthesisDeclarationError: ', f'Did not declare or unintentional declaration of extra parenthesis')

  # opening parenthesis
  if code_array[1] == open_curly_brackets:
    garbage_collect()
  else:
    error('InvalidParenthesisDeclaration: ', f'Did not declare space for {double_quote}venv{double_quote}')
  if code_array[-1] == close_curly_brackets:
    garbage_collect()
  else:
    error('InvalidParenthesisDeclaration: ', f'Did not declare space for {double_quote}venv{double_quote}')

def run_main_code_compiler():                                     #
  return_code_on_success = ''
  
  
  
  main_console_call = 'main.console'
  main_void_call = 'main.void'
  
  
  try:
    call_func_by_client = code_array[2]
    
    call_func_by_client_by_parts = call_func_by_client.split('(')
    call_func_by_client_part_one = call_func_by_client_by_parts[0]
    call_func_by_client_part_two = call_func_by_client_by_parts[1]
  except IndexError:
    error('InsecureDeclarationForMainClass: ', 'No use of brackets for secure declaration of main/{class}')
  
  if call_func_by_client_part_one == main_console_call:
    garbage_collect()
    run_main_console_code = true
    run_main_void_code = true
  elif call_func_by_client_part_one == main_void_call:
    run_main_console_code = false
    run_main_void_code = true
    garbage_collect()
  else:
    error('InvalidCallForMainClass: ', f'No call {double_quote}{call_func_by_client_part_one}{double_quote}')
  
  if call_func_by_client_part_two[-1] == close_brackets:
    garbage_collect()
  else:
    error('InsecureDeclarationForMainClass: ', 'No use of brackets for secure declaration of main/{class}')
  return_code_on_succes_word_count = len(call_func_by_client_part_two) - 1
  for i in range(return_code_on_succes_word_count):
    return_code_on_success = return_code_on_success + call_func_by_client_part_two[i]

  
  if code_array[3] == open_curly_brackets:
    garbage_collect()
  else:
    error('ParenthesisError: ', 'seems like you forgot the use of parenthesis for main.class')
  
  if code_array[-2] == close_curly_brackets:
    garbage_collect()
  else:
    error('ParenthesisError: ', 'seems like you forgot the use of parenthesis for main.class')
  
  if run_main_console_code == true:
    garbage_collect()
  elif run_main_void_code == false:
    garbage_collect()
  else:
    error('InvalidMainClassError: ', 'invalid class declaration for the program')
  
  return return_code_on_success + '^%^%^%^%^%^' + run_main_console_code

def run_main_console_code(return_code_on_success):                                      #
  import re
  
  def remove_last_two_words(text):
    # Split the text into a list of words with their leading and trailing spaces
    words = re.findall(r'\S+\s*', text)
    
    # Check if there are fewer than two words
    if len(words) <= 2:
        return ''  # Return an empty string if there are fewer than or exactly two words
    
    # Remove the last two words
    remaining_words = words[:-2]
    
    # Join the remaining words back into a string
    result = ''.join(remaining_words)
    
    return result
  
  def remove_first_four_words(text):
    # Regular expression to match the first four words and any surrounding spaces
    # \s+ matches one or more whitespace characters (spaces, tabs, etc.)
    pattern = re.compile(r'(\S+\s+){4}')
    patern_for_behind = re.compile(r'(\S+\s+){0}')
    # Use sub to remove the first four words while keeping the rest of the text intact
    result = pattern.sub('', text, count=1)
    result = patern_for_behind.sub('', result, count=1)
    return result
  
  main_code = remove_first_four_words(code)
  main_code = remove_last_two_words(main_code)
  
  main_code_elements = main_code.split('\n')
  for i in range(len(main_code_elements)):
    main_code_elements[i] = main_code_elements[i].strip()
  main_code_elements = [x for x in main_code_elements if x != null]
  main_code_elements = [x for x in main_code_elements if x[0] != comment_hash]
  
  
  for i in range(len(main_code_elements)):
    if main_code_elements[i][-1] == ';':
      garbage_collect()
    else:
      error('IndentationError: ', f'no proper line-end for {double_quote}{main_code_elements[i]}{double_quote}')
  
  main_commands_compiler(main_code_elements)
  
user_input = input(Fore.GREEN + '$ ' + Fore.RESET)                #
user_input_bits = user_input.split(' ')                           #
obl_compile_command = 'obl.compile'                               #
if user_input_bits[0] == obl_compile_command:
  obl_file_name = user_input_bits[1]                              #
  try:
    with open(obl_file_name, 'r') as file:
      code = file.read()                                            #
      file.close()
  except FileNotFoundError:
    error('FileNotFoundError: ', f'No such file or directory: {double_quote}{obl_file_name}{double_quote}')
else:
  error('CommandCallError: ', f'command {double_quote}{user_input_bits[0]}{double_quote} does not exist.')

virtual_environment_variable = 'venv'                             #
code_array = code.split()

input_venv_variable = code_array[0]

if input_venv_variable == virtual_environment_variable:
  run_basic_code_compiler()
  call_value = run_main_code_compiler()
  if call_value.split('^%^%^%^%^%^')[1] == true:
    run_main_console_code(call_value.split('^%^%^%^%^%^')[0])
  elif call_value.split('^%^%^%^%^%^')[1] == false:
    print('Void')
else:
  error('VirtualEnvironmentDeclarationError: ', f'Invalid declaration of virtual-environment')
  
return_code(call_value.split('^%^%^%^%^%^')[0])