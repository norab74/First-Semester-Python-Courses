"""
    What happens to data stored in a Python variable after the program ends?
        It is released by the garbage collector
    Have you ever saved a doc, image, video? What type of file was it?
        PNG, MKV, JPG, TXT, DOC
    What is the difference between temporary data (in RAM) and permanent data (on Disk)?
        RAM is volatile, when power is removed it will be lost, it is also much faster.
        Permanent data is stored with persistence, on non-volatile memory such as NAND Flash or Magnetic Platters
    Why might a program want to store data permanently?
        Persistent memory is helpful when an application wants to be used over time, rather than as a oneshot
    How do we define a file?
        Give it a name. 
        Choose a place for it.
    Plaintext files like TXT and CSV are easy to work with, no special tools necessary.
        More complicated files like Mircosoft's proprietary DOCX implementation may require
            specialized tools to access
    
Files:
    Files allow us to save and retrieve data to the Disk
    They allow data to persist between sessions.
    Without files, everything would be lost when an app closes.
    As a Programmer, it is best to think of files like containers which store data.
    
    
Opening a file in Python:
    Use the Open Command:
        open(name,mode,buffering)
                #mode and buffering are optional params.
                Mode determines how the file get's opened
                    'r' - Read Only
                    'w' - Write Only
                    'a' - Append (write only at EOF)
                    'b' - Binary Mode
                    '+' - RW (add to other mode)
                Buffering:
                    0 is unbuffered
                    1 or any negative is buffered with default values
                    any other number sets the buffer size in bytes
            Example:
            
            file = open('exampleDir/exampleFile.txt', w+)
            
            
        
    
Plaintext files: These filetypes are designed to be readable as a human
    .txt
    .py
    .html
    .md
    .csv
    
Binary files: These need special tools to read, since they're not made for humans
    .jpg
    .exe
    .elf
    .mp3
    .mp4
    .png
    
    
Great, so what do we do with it?
    Open a file. 
    Read the contents.
    Write to a file.
    Close the file. - Extremely important especially in COW situations like if you're running scripts at system level on btrfs
        You should open the file buffered in this case
        
        
        
What does it mean to iterate over a file?
    Iterating over a file means to read from the file and perform an operation on the data returned.
        The simplest example of this is a simple "while contents:" loop where contents = file.read(1) performing an action upon contents
        This is a bytewise iterant operation of the file.
            Bytewise iterant operations can be used for removal of certain characters for input sanitization (for web app security for example)
        One may also have a linewise iterant:
            contents = file.readline(1)
        Python does not include a bitwise iterator, but one can be simply implemented.
    Reading a file in Basic Iteration is recommended for proper management of memory. Don't pull in more bullshit than you need.
    Alternatively, you may read the entire file at one time. You probably shouldn't do this in most circumstances.
    
    """