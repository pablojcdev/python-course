def say_hi():
    print("Hello user")

say_hi()

def say_hi(name):
    print("Hello " + name)

say_hi("Mike")
say_hi("Steve")

def say_hi(name, age):
    print("Hello " + name + ". You are " + age)

say_hi("Mike", "35")
say_hi("Steve", "32")

def say_hi(name, age):
    print("Hello " + name + ". You are " + str(age))

say_hi("Mike", 35)
say_hi("Steve", 32)