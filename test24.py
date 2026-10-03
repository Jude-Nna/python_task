# a basic search engine that tells whether a name is in the list or not
names=["Paul","Peter","Oli","Olisa","Austin"]
search_name=input(("Enter your name: "))
found = False
for name in names:
    if search_name == name:
        print("The name is in the list")
        found = True
        break
 
 
if not found:
    print("Name not found")