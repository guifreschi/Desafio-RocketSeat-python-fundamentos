from stylization import lines, end, msg_lines, clear_terminal, error_msg
from colorama import init, Fore, Back, Style
from time import sleep
from actions import *

init()

def show_options():
  while True:
    clear_terminal()
    lines()
    msg_lines('Opções de Agenda')
    print("[1] - Adicionar Contato")
    print("[2] - Visualizar Lista de Contato")
    print("[3] - Editar Contato")
    print("[4] - Favoritar ou Desfavoritar Contato")
    print("[5] - Listar Contatos Favoritos")
    print("[6] - Apagar Contato")
    print(Style.BRIGHT + Fore.RED + "[7] - Sair" + Style.RESET_ALL)
    sleep(0.2)
    error = False
    choice = str(input('Escolha: '))
    if not choice.isnumeric():
      error = True
    else:
      choice = int(choice)

    if error:
      error_msg("Opção Inválida! Digite um número.")

    if choice == 1:
      while True:
        clear_terminal()
        add_contato()
        continuar = input('Deseja continuar [S/N]? ').lower()
        if not continuar:
          print('Nenhuma resposta... Encerrando.')
          break
        if continuar == 'n':
          break
        
    elif choice == 2:
      clear_terminal()
      visualizar_contato()
    elif choice == 3:
      clear_terminal()
      editar_contato()
    elif choice == 4:
      clear_terminal()
      favoritar()
    elif choice == 5:
      clear_terminal()
      listar_favoritos()
    elif choice == 6:
      clear_terminal()
      remove_ctt()
    elif choice == 7:  
      msg_lines('FIM')
      break
    else:
      if not error:
        error_msg(time=0.7)

show_options()
