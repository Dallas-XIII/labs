x = 10
z = 23

def func():
    a = 20
    def func1():
        nonlocal a
        a =a + 1
        print(a)
        def func2():
            nonlocal a
            a = a + 2
            print(a)
            
        func2()
        
    func1()
    
func()