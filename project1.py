N = int(input("Введіть значення N: "))

with open('output.txt', 'w') as file:
    for i in range(1, N + 1):
        power_of_3 = 3 ** i
        file.write(f"3^{i} = {power_of_3}\n")

print(f"Результати були записані у файл 'output.txt'.")
