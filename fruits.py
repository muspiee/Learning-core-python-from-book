FRUITS = ['mango','banana','orange','apple','pineapple']
FRUITS.sort()
print(FRUITS)
opp = input('Add or Remove?:  ')
if opp == 'Add':
    item_add = input("What do you want to add?:  ")
    FRUITS.insert(0, item_add)
    print(FRUITS)
else:
    item_remove = input("What do you want to remove?:  ")
    if item_remove in FRUITS:
        FRUITS.remove(item_remove)
        print(FRUITS)
    else:
        print(item_remove, "not found")


    

