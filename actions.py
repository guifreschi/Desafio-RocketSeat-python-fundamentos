from stylization import lines, end, msg_lines, clear_terminal, error_msg

contacts = []

def add_contato():
  lines()
  msg_lines('Adicionar Contato')
  print()

  nome = ''
  telefone = ''

  while not nome:
    nome = input('Digite o nome do contato: ')

    if not nome:
      error_msg('Nome Necessário!', 0.5)
  print()

  while not telefone:
    telefone = str(input('Digite o telefone do contato: '))

    if not telefone:
      error_msg('Telefone Necessário!', 0.5)
  print()

  email = input('Digite o email do contato (opcional): ')
  if not email:
    print('Contato Adicionado sem e-mail.')
    email = 'E-mail não adicionado.'
  print()
  
  favorito = input('Deseja favoritar o contato [S/N]? ').lower()
  if not favorito:
    favorito == False
    print('Contato não favoritado.')
  if favorito == 's':
    favorito = True
    print('Contato Favoritado')  
  elif favorito == 'n':
    favorito = False
  print()

  nome = f"{nome} {'⭐' if favorito else ''}"

  contact = {f'Nome': nome, 'Telefone': telefone, 'E-mail': email, 'Favorito': favorito}
  contacts.append(contact)
  msg_lines('Contato Adicionado!')

def visualizar_contato():
  lines()
  msg_lines('Lista de Contatos:')
  if contacts:
    print(f'Você possui {len(contacts)} contatos:')
    print()
    for contact in contacts:
      print(f'Nome: {contact['Nome']}')
      print(f'Telefone: {contact['Telefone']}')
      print(f'E-mail: {contact['E-mail']}')
      lines()
  else:
    print('Você ainda não possui contatos...')
  input('> Sair...')

def editar_contato():
  lines()
  msg_lines('Editar Contato')
  i = 0
  if contacts:
    for contact in contacts:
      i += 1
      print(f'{i}- {contact['Nome']}')
    error = False
    choice = str(input('Qual contato deseja modificar? '))
    if not choice.isnumeric():
      error = True
      error_msg("Opção Inválida! Digite um número.")
    else:
      choice = int(choice) - 1

    if not error:
      if choice >= len(contacts):
        error_msg()
      else:
        clear_terminal()
        msg_lines('Página de Edição')
        contact = contacts[choice]
        nome = contact['Nome']
        telefone = contact['Telefone']
        email = contact['E-mail']
        favorito = contact['Favorito']

        print(f'1- Nome: {nome}')
        print(f'2- Telefone: {telefone}')
        print(f'3- E-mail: {email}')
        print(f"4- Contato {'favoritado' if favorito else 'não favoritado'}")

        favorito = contacts[choice]['Favorito']
        change = int(input('O que deseja alterar [1-4]? '))

        if change == 1:
          nome = input('Digite o novo nome: ')
        elif change == 2:
          while True:
            telefone = str(input('Digite o novo telefone: '))
            if not telefone:
              error_msg('O telefone não pode ser nulo!')
            else:
              break
        elif change == 3:
          email = input('Digite o novo E-mail: ')
        elif change == 4:
          favorito = not favorito
          print('Contato favoritado!' if favorito else 'Contato removido dos favoritos!')
        else:
          error_msg()
        
        if favorito:
            if ' ⭐' not in nome:
              nome += ' ⭐'
        else:
          if ' ⭐' in nome:
            nome = nome.replace(' ⭐', '')
        contacts[choice] = {'Nome': nome, 'Telefone': telefone, 'E-mail': email, 'Favorito': favorito}
  else:
    print('Você ainda não possui contatos...')
  input('> Sair...')

def favoritar():
  lines()
  msg_lines('Favoritar/Desfavoritar Contato')
  i = 0
  if contacts:
    for contact in contacts:
      i += 1
      print(f'{i}- {contact['Nome']}')
    error = False
    choice = str(input('Selecione quem deseja favoritar/desfavoritar: '))
    if not choice.isnumeric():
      error = True
      error_msg("Opção Inválida! Digite um número.")
    else:
      choice = int(choice) - 1

    if not error:
      if choice >= len(contacts):
        error_msg()
      else:
        favorito = not contacts[choice]['Favorito']
        nome = contacts[choice]['Nome']

        if favorito:
            if ' ⭐' not in nome:
              nome += ' ⭐'
        else:
          if ' ⭐' in nome:
            nome = nome.replace(' ⭐', '')
        contacts[choice]['Nome'] = nome
        contacts[choice]['Favorito'] = favorito
        print('Contato favoritado!' if favorito else 'Contato removido dos favoritos!')
  else:
    print('Você ainda não possui contatos...')
  input('> Sair...')

def listar_favoritos():
  lines()
  msg_lines('Contatos Favoritos')
  i = 0
  if contacts:
    for contact in contacts:
      nome = contact['Nome']
      if ' ⭐' in nome:
        i = 1
        print(f'Nome: {nome}')
        print(f'Telefone: {contact['Telefone']}')
        print(f'E-mail: {contact['E-mail']}')
        lines()
      if i == 0:
        print('Você ainda não possui contatos favoritados!')
  else:
    print('Você ainda não possui contatos...')
  input('> Sair...')

def remove_ctt():
  lines()
  msg_lines('Remover Contato')
  if contacts:
    i = 0
    for contact in contacts:
      i += 1
      print(f'{i}- {contact['Nome']}')
    error = False
    choice = str(input('Selecione quem deseja REMOVER: '))
    if not choice.isnumeric():
      error = True
      error_msg("Opção Inválida! Digite um número.")
    else:
      choice = int(choice) - 1

    if not error:
      if choice >= len(contacts):
        error_msg()
      else:
        confirmação = str(input('Deseja REMOVER o contato [S/N]? ')).lower()
        if confirmação == 's':
          del contacts[choice]
        else:
          print('Remoção Cancelada...')
        print('Contato Removido!')
  else:
    print('Você ainda não possui contatos...')
  input('> Sair...')
