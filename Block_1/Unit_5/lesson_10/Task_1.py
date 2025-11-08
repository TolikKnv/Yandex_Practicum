num_string_1 = "100 13 2 143 12 3 55 4 64 18 56"
num_string_2 = "234 2 56 432 3 100 12 99 43 18 31 64"
num_string_1_list = set(num_string_1.split())
num_string_2_list = set(num_string_2.split())
print(len(num_string_1_list & num_string_2_list))
