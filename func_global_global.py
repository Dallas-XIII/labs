x = 50

def func():
    global x #ссылка на переменную Х из верхнего уровняюделает Х доступым для всего что ниже в ЭТОМ блоке
    
    print('X value is ', x)
    x = 2
    print('X value changed to',x)

func()
print('new X value is',x)
