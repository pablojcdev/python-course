for letter in "Giraffe Academy":
    print(letter)

friends = ["Jim", "Karen", "Kevin"]
for name in friends:
    print(name)

for index in range(10):
    print(index)

#between
for index in range(3, 10):
    print(index)

friends = ["Jim", "Karen", "Kevin"]
for index in range(len(friends)):
    print(friends[index])
    
print(friends[1])

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not first")
