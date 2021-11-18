x = 50
def func(x):
    print('x equal to',x)
    x = 2
    print('attempt to change local X value to', x)
func(x)
print('X value is still',x)
