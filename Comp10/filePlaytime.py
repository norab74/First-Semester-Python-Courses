f = open('Python Fundamentals/Comp10/demo.md' , 'r')
#f.write("\nHello, World!\nI've been Modified!\nDon't Forget to Drink your Ovaltine!\n")
#contents = f.read()
char = f.readlines(1)
while char:
        print(char)
        char = f.readlines(1)