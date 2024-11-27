from time import sleep
import os
from colorama import Fore, Style

def clear_terminal():
  if os.name == 'nt':  
    os.system('cls')
  else:  
    os.system('clear')

def lines(legnth=30):
  print('-=' * legnth)

def msg_lines(msg, length=60):
  print(msg.center(length, '-'))

def end():
  lines()
  print()
  sleep(0.5)

def error_msg(msg="Opção Inválida!", time=1.2):
  print(Fore.RED + msg + Style.RESET_ALL)
  sleep(time)
