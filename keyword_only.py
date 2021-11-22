def total(initial = 5, *S, extra_number):
    count = initial
    for number in S:
        count += number
    count += extra_number
    print(count)
    
total(10, 1, 2, 3, extra_number = 50)
#total(10, 1, 2, 3)