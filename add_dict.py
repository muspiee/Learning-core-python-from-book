dict = {}

a = 0
num = input('How many times do you want to add? ---> ')
num = int(num)

while a < num:
    add_name = input('What is your name? ---> ')
    add_age = input('What is your age? ---> ')
    dict[add_name] = add_age
    print(dict)
    a += 1