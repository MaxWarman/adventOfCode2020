f = open("Day 3 - input.txt")
f1 = f.readlines()
trees_counter = 0
arr = []
for i in range(323):
    arr.append(str(f1[i]))
x=0
for i in range(323):
    txt = ""
    for j in range(31):
        if j==x:
            if str(arr[i][j]) == "#":
                txt = txt + "T"
                trees_counter = trees_counter + 1
            else:
                txt = txt + "@"
        else:
            txt = txt + str(arr[i][j])
    
    print(txt, f"x = {x}")

    if x == 30:
        x = 0
    else:
        x = x + 1

print(trees_counter)