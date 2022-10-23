
numbers = input("Enter 10 int: ").split()
numbers = list(map(int, numbers))
print(len(numbers))

evenlist = []

for i in range(5):
  evenlist.append(numbers.pop(i))


print("The list numbers: ", numbers)
print("The list for even index elements: ", evenlist)
