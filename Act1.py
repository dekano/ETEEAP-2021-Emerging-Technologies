
preLims = int(input("Prelims: "))
midTerm = int(input("Midterm: "))
semiFinal = int(input("Semifinal: "))
finals = int(input("Final: "))

Ave = float((preLims + midTerm + semiFinal + finals) / 4)

if (Ave < 60):
    print("Your grade is E")
elif(Ave >= 61 or Ave <= 70):
    print("Your grade is E")
elif(Ave >= 71 or Ave <= 79):
    print("Your grade is D")
elif(Ave >= 80 or Ave <= 89):
    print("Your grade is C")
elif(Ave >= 90 or Ave <= 98):
    print("Your grade is B")
elif(Ave > 99):
    print("Your grade is A")


