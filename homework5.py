immutable_var = 1, 3, 5, 7, 9
print(immutable_var)
# immutable_var[2] = 1
# print(immutable_var)
print(type(immutable_var))

mutable_list = [1, 3, 5, 7, 9]
print(mutable_list)
print(type(mutable_list))
mutable_list[0] = 3
print(mutable_list)
mutable_list[4] = 1
print(mutable_list)
