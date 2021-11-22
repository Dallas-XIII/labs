def maximum(x: 'первое число', y: 'второе число') -> int:
    if x > y:
       return x
    elif x == y:
       return 'Числа равны.'
    else:
       return y
print(maximum(2, 3))
pass