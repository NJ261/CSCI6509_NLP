#!/usr/bin/env python3

some_list = ["first_name","last_name","age","occupation"]
some_tuple = ("John", "Holloway", 35, "carpenter")

result = {}

for i in range(0, len(some_list)):
	result[some_list[i]] = some_tuple[i]

print(result)
