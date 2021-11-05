
preLims = int(input("Prelims: "))
midTerm = int(input("Midterm: "))
semiFinal = int(input("Semifinal: "))
finals = int(input("Final: "))

Ave = float((preLims + midTerm + semiFinal + finals) / 4)

if (Ave >= 75):
    print("PASSED")
else: 
    print("FAILED")

