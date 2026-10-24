def bse():
    usernames = ['Paul', 'Peter', 'Olisa', 'Austin']
    name = input('Enter your name: ')
    found = False
    for user in usernames:
        if user == name:
            print("the name is in the list")
            found = True
    if found == False:
        print("The name is not on the list")

bse()