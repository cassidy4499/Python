my_list = [] 
unsorted = True 
num = int(input("How many numbers do you want to sort: ")) 
for i in range(num): 
  val = float(input("Enter a number: ")) 
  my_list.append(val) 
while unsorted: 
  unsorted = False 
  for i in range(len(my_list) - 1): 
    if my_list[i] > my_list[i + 1]: 
      unsorted = True 
      my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] 
print("\nSorted:") 
print(my_list)
