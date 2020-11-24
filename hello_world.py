print("Hello World")

l = [1, 2, 3]

if 1 in l:
    print("Am gasit 1")
else:
    print("Nu am gasit 1")


print(id(l))

user_name = "Eddy"

print(id(user_name))

user_name = "Gabi"
print(user_name)

s = """
Pot sa afisez
text cum
        doreste caprioara
"""
print(s)

s = "{} are {} mere".format("Ana", 32)
print(s)

s = "{1} are {0} mere".format("Ana", 32)
print(s)

dollars = 49.23
print(F"I have only {dollars} dollars")


l = [1,2,3, "Eddy", [11,22]]
print(l)
print(l[-2])
print(l[-1])
print(l[0])

number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(F"\n{number_list[4:]}")
print(number_list[-5:])
print(number_list[-1:])

d = {
    1: "Ana",
    2: "are",
    3: "mere"
}

for key, value in d.items():
    print("{} -> {}".format(key, value))

my_listing = [1, 2, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10]
print(my_listing)
my_set = set(my_listing)
print(my_set)

my_listing = [1, 3, 2, 8, 9, 6, 7, 4, 5, 10]
print(F"\n{my_listing}")
my_tup = tuple(my_listing)
print(my_tup)