number = 34
running = True
while running:
    guess = int(input('Введите целое число: '))
    
    if guess == number:
        print('Вы угадали')
       # running = False # выход из цикла
        break
    elif guess < number:
        print('Загаданное число больше')
    else:
        print('Загаданное число меньше')
else: #исполняется по выходу из цикла, когда значение услония становится ложным
    print('Выход из цикла')
print('quit')
