'''BellP3 Notes.txt
    Ok, so in the initialization stage of our app we need to ask the user for a list of qualities to apply.
    How do we interface with that list of qualities as though they are variables? 

    EX:
        in our program we use 
        def generateSampleLists():
            #columnIndex 0            1        2             3           4           rowIndex
                objects=["Apple",    "Banana","Carrot",     "Donut",    "Eclair"]           #0
                quality=["New",      "Fresh" ,  "Poor",  "Fresh Baked", "Stale" ]           #1
                price  =[2.59      ,  .19    ,  .05    ,       .75    ,    .25  ]           #2

                This generates three lists, the titles of which are the qualities I am trying to gather to use as varibles.

                We can use a type hint? 
                        dbList: list[list]      This tells python to treat dbList as a list that may contain lists
                                This should allow us to use dbList[0]=objects for example to insert the list 'objects' into our list dbList as row 1.
                    What if the user wants to define their own qualities?
                        dbList: list[list]
                            dbList[0] = input.str("what quality would you like to use for the first sort category?).trim
                            dbList.append([None]*50)
                            print(f"Database of {dbList[0][1]} successfully initialized")
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            '''