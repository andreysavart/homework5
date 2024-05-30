immutable_var = (1, "hello", [3, 4, 5], 6.7)
print(immutable_var)

#immutable_var[0] = 2  # Это даст ошибку, так как кортежи неизменяемы

mutable_list = [10, 20, 30, 40]
mutable_list[1] = 25
mutable_list.append(50)
print(mutable_list)