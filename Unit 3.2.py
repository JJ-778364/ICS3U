list = []
x = input("How many items are you entering?")
x = int(x)
print("Enter your items below:")
for i in range(x):
  item = input("Item name:")
  list.append(item)
print("You have entered", x, "items.")
for x in list:
  print(x)
