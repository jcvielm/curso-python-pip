import random

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0

rounds = 1

tot_rounds = int(input("Ingrese a cuántas rondas quiere jugar: "))

while True:

  print('*' * 10)
  print(f'ROUND {rounds} (a {tot_rounds})')
  rounds += 1
  print('*' * 10)

  print('computer_wins: ', computer_wins)
  print('user_wins: ', user_wins, '\n')
  
  user_option = input("Favor elegir entre Piedra, Papel o Tijera: ")
  user_option = user_option.lower()
  
  if not user_option in options:
    print('this option is no available. Play again\n')
    continue
    
  computer_option = random.choice(options) # Se importa una libreria de py de donde obtenemos esta funcion para la aletoriedad
  
  print('User option = ', user_option)
  print('Computer option =', computer_option)
  
  # computer_option = round()
  
  if user_option == computer_option:
    print("Empate\n")
  elif user_option == 'piedra':
    if computer_option == 'papel':
      print('Has perdido porque papel gana a piedra \nMal (⁠┛⁠✧⁠Д⁠✧⁠)⁠)⁠┛⁠彡⁠┻⁠━⁠┻\n')
      computer_wins += 1
    else:
      print('Piedra gana tijera. \nHas ganado (⁠◡⁠ ⁠ω⁠ ⁠◡⁠)\n')
      user_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('Has ganado porque papel gana a piedra (⁠◡⁠ ⁠ω⁠ ⁠◡⁠)\n')
      user_wins += 1
    else:
      print('Tijera gana a papel, por eso has perdido (⁠┛⁠✧⁠Д⁠✧⁠)⁠)⁠┛⁠彡⁠┻⁠━⁠┻\n')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'piedra':
      print('has perdido porque piedra gana a tijera (⁠┛⁠✧⁠Д⁠✧⁠)⁠)⁠┛⁠彡⁠┻⁠━⁠┻\n')
      computer_wins += 1
    else:
      print('has ganado. Tijera gana a papel (⁠◡⁠ ⁠ω⁠ ⁠◡⁠)\n')
      user_wins += 1
  if computer_wins == tot_rounds:
    print(f'El ganador es computadora por un tanto de {computer_wins} a {user_wins}')
    break

  if user_wins == tot_rounds:
    print(f'El ganador es usuario por un tanto de {user_wins} a {computer_wins}')
    break
  
'''
print(user_option)
print(computer_option)
'''
