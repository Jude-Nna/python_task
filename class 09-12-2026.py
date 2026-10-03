flashlight_input=(input ("Do you want to bring a flashlight? yes/no"))
if flashlight_input=="yes":
    has_flashlight=True
else:
    has_flashlight = False
print(has_flashlight)
cave_input= input(("Do you see a dark cave. Do not enter? yes/no"))
if cave_input == "yes":
    enter_cave=True
else:
    enter_cave = False
if enter_cave and has_flashlight==True:
    print(" they find treasure.")
elif enter_cave and has_flashlight==False:
    print("hey get lost in the dark!")
else:
    print(" they never entered the cave")
