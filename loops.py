nums =[1,2,3,4,5]

print('###### Normal for loop ######')
for num in nums:
    print(num)

print('###### For loop with a break statement ######')
for num in nums:
    if num == 3:
        print('Number Found')
        break
    print(num)


print('###### For loop with continue ######')
for num in nums:
    if num ==3:
        print("Number Found")
        continue
    print(num)

print('###### While loop ######')
x=0
while x<20:
    print (x)
    x +=1

print("###### While with break ######")
y=0
while y <10:
    if y==6:
        break
    print(y)
    y+=1