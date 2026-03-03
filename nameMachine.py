def nameMachine(name):
    if len(name) <=2:
        name.insert(1, "(no middle name)")
    return name
name = input ( "Type a name: ").split (' ')
print(f"      First Name: {nameMachine(name)[0]} \n      Middle Name: {nameMachine(name)[1]} \n      Last Name: {nameMachine(name)[2]} \n")