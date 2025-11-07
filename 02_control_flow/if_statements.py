print()
print("*** Age Classification Program ***")
print()

edad = int(input("Cual es tu edad?: "))

if edad < 18:
    print("You are minor")

elif edad <= 64:
    print("You are an adult")

else:
    print("You are a senior.")