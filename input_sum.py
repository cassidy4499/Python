my_list = []
num = int(input("How many numbers do you want to sum?: ")) 
for i in range(num):
    val = float(input("Enter a number: ")) 
    my_list.append(val) 
total = 0
for i in my_list:
    total += i
print(total)
