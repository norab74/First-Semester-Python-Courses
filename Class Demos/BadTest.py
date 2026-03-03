class BadTest:
    def show():#Always add self, or the code will not work
        print("This will not work")
            #self can technically be anything, but you really shouldn't
test = BadTest()

test.show()