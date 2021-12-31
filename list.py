friends = ["Kevin", "Karen", "Jim"]

print(friends)

friends = ["Kevin", "Karen", "Jim"]

print(friends[0])

friends = ["Kevin", "Karen", "Jim"]

print(friends[-1])

#Toma todo desde el n°1 (Karen)
friends = ["Kevin", "Karen", "Jim"]

print(friends[1:])

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

#Va a tomar todo desde el 1 hasta el 3, sin contar el 3
print(friends[1:3])

#Aca con el friends[1]= "Mike" se reemplaza el n°1 por "Mike"
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends[1] = "Mike"
print(friends)

lucky_numbers = [4, 8, 3, 12, 54]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
print(friends)

lucky_numbers = [4, 8, 3, 12, 54]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.append("Creed")
print(friends)

lucky_numbers = [4, 8, 3, 12, 54]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.insert(1, "Kelly")
print(friends)

lucky_numbers = [4, 8, 3, 12, 54]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.remove("Jim")
print(friends)

lucky_numbers = [4, 8, 3, 12, 54]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.clear()
print(friends)

lucky_numbers = [4, 8, 3, 12, 54]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.pop()
print(friends)

lucky_numbers = [4, 8, 3, 12, 54]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends.index("Oscar"))

lucky_numbers = [4, 8, 3, 12, 54]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

print(friends.count("Jim"))

lucky_numbers = [4, 8, 3, 12, 54]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.sort()
print(friends)

lucky_numbers = [4, 8, 3, 12, 54]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers = [4, 8, 3, 12, 54]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
lucky_numbers.reverse()
print(lucky_numbers)


lucky_numbers = [4, 8, 3, 12, 54]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

friends2 = friends.copy()
print(friends2)