D = {}

with open('input.txt', 'r') as file:
    text = file.read()
    text = text.lower()
    for char in text:
        if 'a' <= char <= 'z':
            if char in D:
                D[char] += 1
            else:
                D[char] = 1

print("Частота появи літер в тексті:")
print(D)
