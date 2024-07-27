li = [1,2,3,4,5,2,1,1,2,2,3,3,4]
cnt = {}
for element in li:
    if element not in cnt.keys():
        print("Found new element!!!")
        cnt[element] = 1
    else:
        cnt[element] += 1