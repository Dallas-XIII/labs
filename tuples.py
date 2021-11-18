
tuple_value = '1','2','3'
tuple_value_2 = '4','5','6','7'
tuple_value_3 = tuple_value_2,'8','9','10'
print(len(tuple_value))
print(len(tuple_value+tuple_value_2))
print(tuple_value_3)
print(tuple_value_3[0][0],tuple_value_3[1])
print(len(tuple_value_3))
print(len(tuple_value_3[0])+len(tuple_value_3)-1)
##tuple_value_3[0][0] = 5            TypeError: 'tuple' object does not support item assignment   
##print(len(turple_value_3))
print('__len__():',tuple_value_3.__len__()) #len()  делает то же самое

