values = [1, 2, "max", 3.3] #list

print(values[0])
print(values[-1])
print(values[1:4])
values.insert(3, "Cool!")
print(values[1:4])
values.append("End")
print(values)
values[2] = "MAX"
print(values)
del values[1 ]
print(values)

val = ( 1, 2, "max", 4.6) #Tuple
print(val[1])

dic = {"a":2, 4:"abcd", "c": "Max"} #Dictionary
print(dic[4])
print(dic["c"])

dict = {}
dict["firstname"] = "Max"
dict["lastname"] = "Savchenko"
print(dict)
print(dict["lastname"])
