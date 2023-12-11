warrior = {"Power": 85, "Heart_Point": 100, "Armor": 30}
wizard = {"Power": 120, "Heart_Point": 140, "Armor": 10}
def shoot(shooter: dict, shooted: dict):
    diminishing = shooter["Power"]-shooted["Armor"]
    shooted["Heart_Point"] -= diminishing

print("Warrior :", warrior)

print("Wizard: ", wizard)

while warrior["Heart_Point"] > 0 and wizard["Heart_Point"] > 0:
    input("Press enter to shoot!!")
    shoot(warrior, wizard)
    print("The warrior attacked the wizard!!!")
    print("Warrior \U00002694 Wizard")
    print("Warrior's heart point \U00002665:", warrior["Heart_Point"])
    print("Wizard's heart point \U00002665:", wizard["Heart_Point"])

    if wizard["Heart_Point"] <= 0:
        break

    input("Press enter to shoot!!")
    shoot(wizard, warrior)
    print("The wizard attacked the warrior!!!")
    print("Wizard \U00002694 Warrior")
    print("Warrior's heart point \U00002665:", warrior["Heart_Point"])
    print("Wizard's heart point \U00002665:", wizard["Heart_Point"])

if warrior["Heart_Point"] <= 0 and wizard["Heart_Point"] <= 0:
    print("Game Over")
    print("It's a draw!")
elif warrior["Heart_Point"] > 0 and wizard["Heart_Point"] <= 0:
    print("Game Over")
    print("The warrior win \U0001F3C6")
else:
    print("Game Over")
    print("The wizard win \U0001F3C6")