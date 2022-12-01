f = open("Day 2 - input.txt")
f1 = f.readlines()
pass_counter = 0

for i in range(1000):
    arr = f1[i].split()
    rang = arr[0].split("-")

    if (arr[2][int(rang[0])-1] == arr[1][0] and arr[2][int(rang[1])-1] != arr[1][0]) or (arr[2][int(rang[0])-1] != arr[1][0] and arr[2][int(rang[1])-1] == arr[1][0]):
        pass_counter = pass_counter + 1

print(pass_counter)
