# sum = 0
# i =10
# while i<1:
#     sum = sum + i
#     sum = sum *2
#     i -=1

# print(sum)



# def rec(string):
#     if len(string) == 1:
#         return string

#     first_char = string[0]
#     last_chars = string[1:len(string)]

#     return rec(last_chars) + first_char

# print(rec("1234"))

x = [1,2,3,4,5,6]

print(x[0:])


def func(items):
    i = 0
    while i <len(items):
        if(len(items[i]) == 0):
            del items[i]

        i += 1

    print(items)

names = ["Rachel", " ", "Medhana","", " ","Tim"]

func(names)
print(names)
import math
print(math.floor(-5.7))
print(round(-5.))


def treee(li):
    root = {}
    for sentence in li:
        base = root
        for word in sentence.split(" "):
            if not base.get(word):
                base[word] = {}
            base = base[word]

    return root

tree = treee(["Hello World", "Hello there "])
print(tree)