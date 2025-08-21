x =  ['tejas', 65,2.5,41]
for i in x:
    print(i)

y = 'tejas'
for i in y:
    print(i, end='')

print()


for i in range(1, 6):
    print("Tejas learns Python", end=", ")
    for j in range(1, 6):
        print(f"every day {j}", end=", ")
    print()


for i in [2,6,'tejas']:
    print(i, end=', ')
print()

for i in range(10): # print values from 0 to 9
    print(i, end=', ')
print()

for i in range(5, 10): #print from 5 to 9
    print(i, end=', ')
print()

for i in range (5,20, 2): #print from 5 to 9 with step 2
    print(i, end=', ')
print()

for i in range(10, 0, -1): #print from 10 to 1
    print(i, end=', ')
print()

for i in range(1,21): # print from 1 to 20 where i is not a multiple of 5
    if i % 5 != 0:
        print(i, end=", ")
print()