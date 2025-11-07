print()
print("*** Voting Selector Program ***")
print()

age = int(input("How old are you?: "))
nationality = input("What is your nationality? German or Colombian: ")
nationality = nationality.lower()

if age >= 18 and nationality == "German":
    print("You can vote in Germany.")

elif age >= 18 and nationality == "Colombian":
    print("You can vote too in Germany")

elif age < 18 or (nationality != "german" and nationality != "colombian"):
    print("You must to be have more than 17 years old and you must be German Or Colombian")

else:
    print("You cannot vote in Germany.")